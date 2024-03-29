from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('attribute', 'value')

    def __str__(self):
        return f'{self.attribute} - {self.value}'


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} - {self.attribute_value.attribute.name} - {self.attribute_value.value}'


class ProductAttributeDefinition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    required = models.BooleanField(default=False)
    read_only = models.BooleanField(default=False)
    default_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE, null=True)
    possible_values = models.ManyToManyField(AttributeValue, related_name='possible_values', blank=True)

    def clean(self):
        self.clean_fields()
        super().clean()

    def __str__(self):
        return f'{self.product.name} - {self.attribute.name}'

