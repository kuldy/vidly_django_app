from django.contrib import admin
from . import models


@admin.register(models.Tag)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'label']
    search_fields = ['label']
