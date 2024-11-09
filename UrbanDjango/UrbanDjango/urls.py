"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from task2.views import page_func, page_class
from task4.views import get_platform, get_games, get_cart
from task5.views import sign_up_by_django,sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', page_func),
    path('class/', page_class.as_view()),
    path('platform/', get_platform),
    path('games/', get_games),
    path('cart/', get_cart),
    path('sign_dj/', sign_up_by_django),
    path('sign_html/', sign_up_by_html)
]
