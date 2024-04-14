from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

from .forms import ProductForm
from .models import User, Order, Product


def index(request):
    return render(request, "homeWork4/index.html")


def basket(request, user_id):
    products = []
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user).all()
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    return render(request, 'homeWork4/user_all_orders.html', {'user': user, 'orders': orders, 'products': products})


def sorted_basket(request, user_id, days_ago):
    products = []
    product_set=[]
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user, date_ordered__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'homeWork4/user_all_product.html', {'user': user, 'product_set': product_set, 'days': days_ago})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                quantity=form.cleaned_data['quantity'],
                time_stamp_on_create=now(),
            )
            product.save()
    else:
        form = ProductForm()
    context = {'form': form, 'title': 'Форма создания нового товара'}
    return render(request, 'hw4_app/create.html', context)


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
    form = ProductForm(instance=product)
    context = {'product': product, 'form': form, 'title': 'Форма обновления данных товара'}
    return render(request, 'hw4_app/update.html', context)
