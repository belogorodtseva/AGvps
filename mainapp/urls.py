from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^en/contact/', views.contact, name='contact'),
    url(r'^en/services/', views.services, name='services'),
    url(r'^en/architecture/', views.architecture, name='architecture'),
    url(r'^en/design/', views.design, name='design'),

    url(r'^ru/home/', views.ruindex, name='ruindex'),
    url(r'^ru/contact/', views.rucontact, name='rucontact'),
    url(r'^ru/services/', views.ruservices, name='ruservices'),
    url(r'^ru/architecture/', views.ruarchitecture, name='ruarchitecture'),
    url(r'^ru/design/', views.rudesign, name='rudesign'),

    url(r'^ua/home/', views.uaindex, name='uaindex'),
    url(r'^ua/contact/', views.uacontact, name='uacontact'),
    url(r'^ua/services/', views.uaservices, name='uaservices'),
    url(r'^ua/architecture/', views.uaarchitecture, name='uaarchitecture'),
    url(r'^ua/design/', views.uadesign, name='uadesign'),

    url(r'^en/archproject/(?P<pk>[0-9]+)/', views.archproject, name='archproject'),
    url(r'^en/designproject/(?P<pk>[0-9]+)/', views.designproject, name='designproject'),
    url(r'^ru/archproject/(?P<pk>[0-9]+)/', views.ruarchproject, name='ruarchproject'),
    url(r'^ru/designproject/(?P<pk>[0-9]+)/', views.rudesignproject, name='rudesignproject'),
    url(r'^ua/archproject/(?P<pk>[0-9]+)/', views.uaarchproject, name='uaarchproject'),
    url(r'^ua/designproject/(?P<pk>[0-9]+)/', views.uadesignproject, name='uadesignproject'),


    url(r'^thanks/$', views.thanks, name='thanks'),
    ]
