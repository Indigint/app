from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app.views.index', name='index'),
    url(r'^index/$', 'app.views.index', name='index'),
    url(r'^about/$', 'app.views.about', name='about'),
    url(r'^contact/$', 'app.views.contact', name='contact'),
    url(r'^why/$', 'app.views.why', name='why'),
    url(r'register/$', 'app.views.register', name='register'),
    url(r'login/$', 'app.views.login_user', name='login'),

    url(r'^po/', include('inventory.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
