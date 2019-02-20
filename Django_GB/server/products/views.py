import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Product
from .models import Category

def product_list_view(request):

    data = Product.objects.all()
    data1 = Category.objects.all()

    return render(
        request,
        'products/index.html',
        {'object_list': data,
         'object_list1': data1}
    )

def product_detail_view(request, pk):

    data = Product.objects.get(pk=pk)

    return render(
        request,
        'products/detail.html',
        {'object': data}
        #{'object': data[idx]}
    )

def products_cat(request):

    data1 = Category.objects.all()

    return render(
        request,
        'products/product_list.html',
        {'object_list1': data1}
    )

def products_category(request, pk=None):
    print(pk)
    
    links_menu = Category.objects.all()
            
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('cost')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(Category, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('cost')

        content = {
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'products/products_list2.html', content)

    
    same_products = Product.objects.all()[3:5]
    
    content = {
        'title': title, 
        'links_menu': links_menu, 
        'same_products': same_products
    }
    
    return render(request, 'products/products.html', content)
