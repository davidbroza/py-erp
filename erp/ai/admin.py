from django.contrib import admin
from .models import DocumentProcessingTask


# Register your models here.
@register.models(DocumentProcessingTask)
class DocumentProcessingTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "create_at", "update_at", "file", "note")
    list_filter = ("create_at", "update_at")
    search_fields = ("note",)
