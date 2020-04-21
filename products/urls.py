from django.contrib import admin
from django.urls import path


from products.views import product_list_view, product_create_view, dynamic_lookup_view, product_delete_view

app_name = 'products'
urlpatterns = [

    path('', product_list_view, name='product'),
    path('create/', product_create_view, name='create'),
    path('search/<int:id>/', dynamic_lookup_view, name='search-detail'),
    path('delete/<int:id>/', product_delete_view, name='delete'),
]
