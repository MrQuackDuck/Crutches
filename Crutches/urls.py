"""Crutches URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path, re_path
from main import views as views_main
from admin import views as views_admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views_main.index),
    re_path('aboutUs', views_main.aboutUs),
    re_path('allCrutches', views_main.allCrutches),
    path('crutch/<int:id>', views_main.crutch),
    path('search', views_main.search),
    
    path('login', views_admin.login),
    path('authorize', views_admin.authorize),
    re_path('adminPanel', views_admin.admin),
    path('createCrutch', views_admin.createCrutch),
    path('edit/<int:id>', views_admin.editCrutch),
    path('delete/<int:id>', views_admin.delete),
    path('logout', views_admin.logout),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)