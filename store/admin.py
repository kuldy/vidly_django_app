from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.db.models.aggregates import Count
from django.db.models.expressions import Value
from . import models

# search django modelAdmin-> model admin options


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']
    # fields = ['title', 'slug']
    # exclude = ['promotions', 'collection']
    # readonly_fields = ['title']
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory',
                    'inventory_status', 'collection_title']
    list_editable = ['unit_price', 'inventory']
    list_filter = ['collection', 'last_updated', InventoryFilter]
    list_per_page = 3
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

    @admin.action(description="Clear Inventory")
    def clear_inventory(self, request, queryset):
        update_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{update_count} products were successfully updated.',
            messages.ERROR
        )


# admin.site.register(models.Collection)
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']
    search_fields = ['title']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}" >{}</a>', url,
                           collection.product_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count('products'))


@admin.register(models.Promotions)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['descriptions']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['first_name']
    list_display = ['id', 'first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 5
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{}</a>', url, customer.orders)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders=Count('order'))

# StackedInline and TabularInline


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']  # throwing error
    model = models.OrderItem
    extra = 0  # 1 form
    # min_num = 5
    # max_num = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer_first_name']
    list_select_related = ['customer']

    def customer_first_name(self, order):
        return order.customer.first_name
