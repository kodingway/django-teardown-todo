from django.conf.urls import url
from django.shortcuts import render
from . import views

urlpatterns = [
    url(r'^$', lambda req: render(req, 'base.html'), name='home'),
]
