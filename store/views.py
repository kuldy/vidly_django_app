from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializers


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializers(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        return Response('ok')


@api_view()
def product_details(request, id):
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializers(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializers(product)
    return Response(serializer.data)


@api_view()
def collection_detail(request, pk):
    return Response('ok')
