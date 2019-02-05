"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import main.views as main

# from main.views import (
#     index, about, contacts
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', main.contacts),
    path('about/', main.about),
    path('temp1/', main.temp1),
    path('product/', include('main.urls')),
    path('first/', include('main.urls')),
    path('second/', include('main.urls')),
    path('', main.index)
]
