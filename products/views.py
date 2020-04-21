from django.shortcuts import render, get_object_or_404, redirect
from .models import Products
from .forms import ProductForm, RawProductForm
from django.http import Http404


# Create your views here.
# Try again

def product_list_view(request, *args, **kwargs):
    obj = Products.objects.all()
    context = {
        'objects': obj
    }
    return render(request, 'products/product_detail.html', context)


# def product_create_view(request, *args, **kwargs):
#     #my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Products.objects.create(**my_form.cleaned_data)
#             my_form = RawProductForm()
#     else:
#         my_form = RawProductForm()
#     context = {
#         'form': my_form
#     }
#     return render(request, 'products/product_create.html', context)

def product_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Products, id=id)
    # try:
    #    obj = Products.objects.get(id=id)
    # except Products.DoesNotExist:
    #     raise Http404
    context = {
        'objects': obj
    }
    return render(request, "products/product_detail_dynamic.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        # Delete and Confirm
        obj.delete()
        return redirect('/')
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)
