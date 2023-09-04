from django.contrib import admin
from django.urls import path
from pages.views import home_view, main_view
from products.views import product_detail_view, product_create_view, product_delete_view, product_list_view
app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='products'),
    path('<int:my_id>/', product_detail_view, name='product_detail'),
    path('<int:ld>/delete/', product_delete_view, name='product_delete'),
    path('create/', product_create_view, name="create"),
    path('main/', main_view, name='main'),
]