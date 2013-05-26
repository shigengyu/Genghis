'''
Created on 2013-5-25

@author: Univer
'''
from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.index, name='about'),
)