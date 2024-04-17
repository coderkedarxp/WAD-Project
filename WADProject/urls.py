"""
URL configuration for WADProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import yaml
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import os

yaml_path = os.path.join(settings.BASE_DIR, 'key.yaml')
with open(yaml_path, 'r') as file:
    secrets = yaml.safe_load(file)

secret_url=secrets['SECRET']

urlpatterns = [
    path(f'{secret_url}/', include('adminApp.urls')),
    path('',include('TourApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)