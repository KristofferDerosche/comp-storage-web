from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('new/', views.new, name='new_category'),
    path('list/', views.list, name='category_list'),
    path('<int:category_id>/', views.details, name='category_details'),
    path('<int:category_id>/update/', views.update, name='category_update'),
    path('<int:category_id>/delete/', views.delete, name='category_delete'),
    path('', lambda request: redirect('category_list')),
]
