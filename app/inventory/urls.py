from django.conf.urls import patterns, url

from inventory import views

urlpatterns = patterns('',
                       # /po
                       url(r'^$', views.index, name='po_index'),
                       # /po/X/
                       url(r'^(?P<PO_id>\d+)/$', views.po, name='po_view'),
                      )