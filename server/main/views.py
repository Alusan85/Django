from django.shortcuts import render
title = 'Сайт для любителей прибухнуть'

links_menu = [
    {'href': 'first', 'name': 'первый переход из динамического меню - но оно не пашет'},
    {'href': 'second', 'name': 'второй переход из динамического меню - и это тоже'},
    {'href': '', 'name': 'Стоять на месте'},
]

content = {
    'title':title,
    'links_menu': links_menu
}

def index(request):
    return render(
        request,
        'index.html'
    )

def about(request):
    return render(
        request,
        'about.html'
    )

def contacts(request):
    return render(
        request,
        'contacts.html'
    )

def temp1(request):
    return render(
        request,
        'temp1.html',
        content
    )

def product(request):
    return render(
        request,
        'main/product.html'
    )

def first(request):
    return render(
        request,
        'main/first.html'
    )

def second(request):
    return render(
        request,
        'main/second.html'
    )