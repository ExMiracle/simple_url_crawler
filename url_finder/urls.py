from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('find_urls/', views.find_urls, name='find_urls')
]