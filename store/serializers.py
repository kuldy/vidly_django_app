from decimal import Decimal
from django.db.models import fields
from rest_framework import serializers
from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)

    # product_count = serializers.SerializerMethodField(
    #     method_name='count_product'
    # )

    # def count_product(self, collection: Collection):
    #     return collection.objects.prefetch_related('product').count()


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__' # bad practice
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection']
    # price = serializers.DecimalField(
    #     max_digits=6, decimal_places=2, source="unit_price")
    price_with_tax = serializers.SerializerMethodField(
        method_name="calculate_tax")
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )
    # collection = serializers.StringRelatedField()
    # collection = CollectionSerializer()
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail'
    # )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Password did not matched!')
    #     return data

    # def create(self, validate_data):
    #     product = Product(**validate_data)
    #     product.other = 1
    #     product.save()
    #     return product

    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance
