from django.conf.urls import patterns, url

from inventory import views

urlpatterns = patterns('',
                       # /po/
                       url(r'^user/$', views.index, name='po_index'),
                       # /po/admin/
                       url(r'^admin/$', views.admin_index, name='po_admin'),
                       # /po/po_id/
                       url(r'^(?P<PO_id>\d+)/$', views.po, name='po_view'),
                      )