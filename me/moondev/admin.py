from django.contrib import admin
from .models import Printer, PrintJob


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['name', 'ip_address', 'port', 'model', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'ip_address', 'model']
    list_editable = ['is_active']


@admin.register(PrintJob)
class PrintJobAdmin(admin.ModelAdmin):
    list_display = ['printer', 'filename', 'status', 'progress', 'created_at', 'started_at']
    list_filter = ['status', 'created_at']
    search_fields = ['filename', 'printer__name']
    readonly_fields = ['created_at', 'started_at', 'completed_at']

