"""patic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from patic.core.views import home
from patic.reports.views import report
from patic.reports2.views import report2
from patic.reports3.views import report3
from patic.avaliacao.views import avaliacao
from patic.importpa.views import importpa

urlpatterns = [
    path('', home),
    path('report/', report),
    path('report2/', report2),
    path('report3/', report3),
    path('avaliacao/', avaliacao),
    path('importpa/', importpa),
    path('admin/', admin.site.urls),
]