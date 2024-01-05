from django.contrib import admin
from django.urls import path
from .views import index, redirect_urls

urlpatterns = [
    path('', index, name='index'),
    path("admin/", admin.site.urls),
    path('<slug>/', redirect_urls, name='redirect_urls')
]
