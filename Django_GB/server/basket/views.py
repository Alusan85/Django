from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basket.models import Basket
from products.models import Product


def basket_view(request):

    data = Basket.objects.all()

    return render(
        request,
        'basket/basket.html',
        {'object_list': data}
    )

    
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
def basket_remove(request, pk):
    content = {}
    return render(request, 'basket/basket.html', content)