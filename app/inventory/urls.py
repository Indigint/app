from django.conf.urls import patterns, url

from inventory import views

urlpatterns = patterns('',
                       # /inventory
                       url(r'^$', views.index, name='index'),
                       # /inventory/X/
                       url(r'^(?P<PO_id>\d+)/$', views.po, name='po'),
                      )