from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import format_html


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def html_description_of_possbile_configurations(self):
        valid_configurations = self.find_all_product_configuration()
        html = "<ul>"
        for config in valid_configurations:
            config_str = ", ".join([f"{pv.property.name}: {pv.value}" for pv in config])
            html += f"<li>Valid Configuration: {config_str}</li>"
        html += "</ul>"
        # return formatted html
        return format_html(html)

    def find_all_product_configuration(self):
        # Find all possible product configurations
        # 1. Get all properties of the product and all their possible values
        # 2. Find all possible combinations of these values, i.e. all possible configurations
        # 3. Make sure that each configuration is valid, i.e. it satisfies all rules

        properties = self.properties.all()

        property_values_groups = [list(property.values.all()) for property in properties]

        # Find all possible configurations
        from itertools import product

        try:
            configurations = list(product(*property_values_groups))
        except Exception as e:
            print(e)

        # Check if each configuration is valid
        valid_configurations = []
        for config in configurations:
            if self.is_valid_configuration(config):
                valid_configurations.append(config)

        return valid_configurations

    def is_valid_configuration(self, config):
        for rule in self.rules.all():
            if rule.is_satisfied_by(config):
                return True
        return False

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=100)

    def __iter__(self):
        return iter(self.name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "properties"


class PropertyValue(models.Model):
    property = models.ForeignKey(Property, related_name='values', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __iter__(self):
        return self.va
    def __str__(self):
        return f"{self.property.name}: {self.value}"


class ProductProperty(models.Model):
    """
    A product can have multiple properties
    """
    product = models.ForeignKey(Product, related_name='properties', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    required = models.BooleanField(default=False)
    read_only = models.BooleanField(default=False)
    max_values = models.PositiveIntegerField(default=1)
    default_value = models.ForeignKey(PropertyValue, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('product', 'property')
        # plural name
        verbose_name_plural = "product properties"

    def __str__(self):
        return f"{self.property.name} for {self.product.name}"


class Rule(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rules')
    description = models.TextField()

    def apply(self, config):
        # Apply the rule to a configuration
        for condition in self.conditions.all():
            if condition.is_satisfied_by(config):
                for outcome in self.outcomes.all():
                    config = outcome.apply(config)
        return config

    def __str__(self):
        return f'{self.product} - {self.description}'


class Condition(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='conditions')
    property_values = models.ManyToManyField(PropertyValue)

    def is_satisfied_by(self, config):
        for pv in self.property_values.all():
            if pv not in config:
                return False
        return True

    def __str__(self):
        return ", ".join([f"{pv.property.name}: {pv.value}" for pv in self.property_values.all()])


class Outcome(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='outcomes')
    property_values = models.ManyToManyField(PropertyValue)

    def apply(self, property_values: list):
        # remove all values from the list that belong to property, and replace them with the new values
        for pv in self.property_values.all():
            property_values = [x for x in property_values if x.property != pv.property]
            property_values.append(pv)
        return property_values

    def __str__(self):
        return ", ".join([f"{pv.property.name}: {pv.value}" for pv in self.property_values.all()])
