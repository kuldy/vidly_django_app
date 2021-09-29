from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.


def say_hello(request):
    # manager object and query_set
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)
    # list(query_set)
    # query_set[0]

    # Retriving objects
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # product = Product.objects.filter(pk=0).first()

    # Filtering products/ search queryset api to find all type of lookup sets
    query_set = Product.objects.filter(unit_price__gt=200)
    # query_set = Product.objects.filter(unit_price__range=(300, 600))
    # query_set = Product.objects.filter(collection__id__range=(1, 2))
    # query_set = Product.objects.filter(title__contains='Cat')
    # query_set = Product.objects.filter(title__icontains='Cat')
    # query_set = Product.objects.filter(last_updated__year=2021)
    # query_set = Product.objects.filter(last_updated__date='2021-09-02')
    # query_set = Product.objects.filter(description__isnull=True)

    return render(request, 'hello.html', {'kullu': 'Kuldeep Singh', 'products': list(query_set)})
