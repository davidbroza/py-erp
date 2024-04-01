from django.db import models
from django.utils.html import format_html


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def html_description_of_possbile_configurations(self):
        valid_configurations = self.find_valid_configurations_for_product()
        html = "<ul>"
        for config in valid_configurations:
            config_str = ", ".join([f"{pv.property.name}: {pv.value}" for pv in config])
            html += f"<li>Valid Configuration: {config_str}</li>"
        html += "</ul>"
        # return formatted html
        return format_html(html)

    def find_valid_configurations_for_product(self):
        valid_configurations = []

        # find all rules that apply to this product
        all_outcomes = []
        for rule in self.rules.all():
            all_outcomes.extend(rule.outcomes.all())

        # find all possible configurations
        for rule in self.rules.all():
            for condition in rule.conditions.all():
                valid_configurations.append(condition.property_values.all())

        return valid_configurations

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "properties"


class PropertyValue(models.Model):
    property = models.ForeignKey(Property, related_name='values', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.property.name}: {self.value}"


class ProductProperty(models.Model):
    """
    A product can have multiple properties
    """
    product = models.ForeignKey(Product, related_name='properties', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'property')

    def __str__(self):
        return f"{self.property.name} for {self.product.name}"


class ProductPropertyValue(models.Model):
    product = models.ForeignKey(Product, related_name='property_values', on_delete=models.CASCADE)
    property_value = models.ForeignKey(PropertyValue, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'property_value')

    def __str__(self):
        return f"{self.property_value.property.name}: {self.property_value.value} for {self.product.name}"


class Rule(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rules')
    description = models.TextField()

    def __str__(self):
        return f'{self.product} - {self.description}'


class Condition(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='conditions')
    property_values = models.ManyToManyField(PropertyValue)

    class ConditionType(models.TextChoices):
        AND = 'AND'
        OR = 'OR'

    def __str__(self):
        return ", ".join([f"{pv.property.name}: {pv.value}" for pv in self.property_values.all()])


class Outcome(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='outcomes')
    property_values = models.ManyToManyField(PropertyValue)

    def __str__(self):
        return ", ".join([f"{pv.property.name}: {pv.value}" for pv in self.property_values.all()])
