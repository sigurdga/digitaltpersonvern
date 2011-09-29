from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'digitaltpersonvern.views.home', name='home'),
    # url(r'^digitaltpersonvern/', include('digitaltpersonvern.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {'template': 'base.html'}),
)
