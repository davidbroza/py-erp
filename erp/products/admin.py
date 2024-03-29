from django.contrib import admin

# Register your models here.

from .models import *


class ProductAttributeDefinitionInline(admin.TabularInline):
    model = ProductAttributeDefinition
    extra = 0
    show_change_link = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeDefinitionInline]
    list_display = ["name"]


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [AttributeValueInline]


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ["attribute", "value"]


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ["product", "attribute_value"]


@admin.register(ProductAttributeDefinition)
class ProductAttributeDefinitionAdmin(admin.ModelAdmin):
    list_display = ["product", "attribute", "required", "read_only", "default_value"]
