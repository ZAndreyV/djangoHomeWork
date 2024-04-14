from django.urls import path
from .views import index, create_product, update_product
from .views import basket, sorted_basket


urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('user/<int:user_id>/', basket, name='basket'),
    path('user_sorted/<int:user_id>/<int:days_ago>/', sorted_basket, name='sorted_basket'),
    path('product/new', create_product, name='create_product'),
    path('product/<int:product_id>/edit', update_product, name='update_product'),
]
