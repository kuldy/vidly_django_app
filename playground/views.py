from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.


def say_hello(request):
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)
    # list(query_set)
    # query_set[0]

    return render(request, 'hello.html', {'kullu': 'Kuldeep Singh'})
