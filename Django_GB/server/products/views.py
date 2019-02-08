import json
from django.shortcuts import render

from .models import Product

def product_list_view(request):

    data = Product.objects.all()

    return render(
        request,
        'products/index.html',
        {'object_list': data}
    )

def product_detail_view(request, pk):

    data = Product.objects.get(pk=pk)

    return render(
        request,
        'products/detail.html',
        {'object': data}
        #{'object': data[idx]}
    )
