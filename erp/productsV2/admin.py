from django.contrib import admin

# Register your models here.

from .models import *


class RuleInline(admin.TabularInline):
    model = Rule
    extra = 0
    show_change_link = True

    fields = ["description", "html_conditions", "html_outcomes"]
    readonly_fields = ["html_conditions", "html_outcomes", "description"]

    @admin.display(description="Conditions")
    def html_conditions(req, obj):
        return format_html("<br>".join([str(o) for o in obj.conditions.all()]))

    @admin.display(description="Outcomes")
    def html_outcomes(req, obj):
        return format_html("<br>".join([str(o) for o in obj.outcomes.all()]))


class ConditionInline(admin.TabularInline):
    model = Condition
    extra = 0


class OutcomeInline(admin.TabularInline):
    model = Outcome
    extra = 0


class ProductPropertyValueInline(admin.TabularInline):
    model = ProductPropertyValue
    extra = 0


class PropertyValueInline(admin.TabularInline):
    model = PropertyValue
    extra = 0


class PropertyInline(admin.TabularInline):
    model = Property
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ["name", "html_configurations"]
    list_display = ["name", "html_configurations"]
    inlines = [ProductPropertyValueInline, RuleInline]

    readonly_fields = ["html_configurations"]

    def html_configurations(self, obj):
        return obj.html_description_of_possbile_configurations()


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [PropertyValueInline]


@admin.register(PropertyValue)
class PropertyValueAdmin(admin.ModelAdmin):
    list_display = ["property", "value"]


@admin.register(ProductPropertyValue)
class ProductPropertyValueAdmin(admin.ModelAdmin):
    list_display = ["product", "property_value"]


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    inlines = [ConditionInline, OutcomeInline]


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ["rule"]


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ["rule"]
