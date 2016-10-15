from django.conf.urls import url
from django.shortcuts import render
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^todo/list/', views.list_view, name='todo-list'),
    url(r'^todo/add/', views.add_view, name='todo-add'),
    url(r'^todo/([0-9]+)/edit', views.edit_view, name='todo-edit'),
]
