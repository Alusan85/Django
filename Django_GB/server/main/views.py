from django.shortcuts import render

from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse


def index(request):
  
    template = get_template(
        'main/index.html'
    )
    context = {
        'name': 'User'
    }
    return HttpResponse(
        template.render(context)
    )

def about(request):
    return render(
        request,
        'main/about.html',
        {
            'about_text': 'Это страница о Проекте'
        }
    )

def contacts(request):
    rendered_page = render_to_string(
        'main/contacts.html',
        {
            'contacts': [
                'Путеводитель',
                'Продажа сувенирной продукции',
                'Инструктаж',
            ]
        }
    )
    return HttpResponse(
        rendered_page
    )
