from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Order, OrderItem, Product

# Create your views here.


def say_hello(request):
    query_set = 'abc'
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
    # query_set = Product.objects.filter(unit_price__gt=200)
    # query_set = Product.objects.filter(unit_price__range=(300, 600))
    # query_set = Product.objects.filter(collection__id__range=(1, 2))
    # query_set = Product.objects.filter(title__contains='Cat')
    # query_set = Product.objects.filter(title__icontains='Cat')
    # query_set = Product.objects.filter(last_updated__year=2021)
    # query_set = Product.objects.filter(last_updated__date='2021-09-02')
    # query_set = Product.objects.filter(description__isnull=True)

    # query_set = Product.objects.filter(inventory__lt=20, unit_price__lt=300)
    # query_set = Product.objects.filter(inventory__lt=20).filter(unit_price__lt=300)
    # query_set = Product.objects.filter(
    #     Q(inventory__lt=20) | Q(unit_price__lt=401))
    # query_set = Product.objects.filter(
    #     Q(inventory__lt=20) | ~Q(unit_price__lt=401))

    # query_set = Product.objects.filter(inventory=F('unit_price'))
    # query_set = Product.objects.filter(inventory=F('collection__id'))

    # query_set = Product.objects.order_by('title')
    # query_set = Product.objects.order_by('-title')
    # query_set = Product.objects.order_by('unit_price', '-title')
    # query_set = Product.objects.order_by('unit_price', '-title').reverse()
    # query_set = Product.objects.filter(collection__id=1).order_by('unit_price')
    product = Product.objects.order_by('unit_price')[0]  # returns product obj
    # product = Product.objects.earliest('unit_price')  # returns product obj asc
    # product = Product.objects.latest('unit_price')  # returns product obj desc

    # query_set = Product.objects.all()[:2]
    # query_set = Product.objects.all()[2:4]

    # query_set = Product.objects.values('id', 'title')
    # query_set = Product.objects.values('id', 'title', 'collection__title')
    # query_set = Product.objects.values_list('id', 'title', 'collection__title')

    # query_set = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    # query_set = Product.objects.only('id', 'title')
    # query_set = Product.objects.defer('description')

    # select_related(1)
    # prefetch_related(n)
    # query_set = Product.objects.select_related('collection').all()
    # query_set = Product.objects.prefetch_related('promotions').all()
    # query_set = Product.objects.prefetch_related(
    #     'promotions').select_related('collection').all()
    orders = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    return render(request, 'hello.html', {'kullu': 'Kuldeep Singh', 'products': list(query_set), 'rohit': product, 'orders': list(orders)})
