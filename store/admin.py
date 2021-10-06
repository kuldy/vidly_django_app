from django.contrib import admin
from . import models

# search django modelAdmin-> model admin options


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory',
                    'inventory_status', 'collection_title']
    list_editable = ['unit_price', 'inventory']
    list_per_page = 3
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


admin.site.register(models.Collection)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 5


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer_first_name']
    list_select_related = ['customer']

    def customer_first_name(self, order):
        return order.customer.first_name
