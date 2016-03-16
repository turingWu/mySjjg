"""mySjjg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from sjjgWeb.views import *
from mySjjg.settings import BASE_DIR,MEDIA_ROOT
urlpatterns = [
    url(r'^ckeditor',include('ckeditor_uploader.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    url(r'^index$',index,name='homepage'),
    url(r'^login$',do_login,name='login'),
    url(r'^reg',register),
    url(r'^matchId',matchId),
    url(r'^test$',test),
    url(r'^index/(?P<root>\d)/(?P<node>\d)/$',information,name='information'),
    url(r'^index/(?P<root>\d)/(?P<node>\d)/(?P<bottom>\d)/$',information),
    url(r'^uploadimg/',upload_image),
    url(r'^media(?P<path>.*)$', 'django.views.static.serve',{'document_root': MEDIA_ROOT}),
    url(r'^upload/(?P<path>(\S)*)','django.views.static.serve',{'document_root':BASE_DIR+'\upload'}),
    url(r'^download/',big_file_download,name='download'),
    url(r'^getTest',getTest,name='getTest'),
    url(r'^homework$',upHomework,name='homework'),
    url(r'^connectUs$',connectUs, name = 'connect'),
    url(r'^logout',do_logout,name='logout'),
    url(r'comment',do_comment,name='comment'),
]

