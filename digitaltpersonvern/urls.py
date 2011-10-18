from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

from views import IndexView
from samklang_pages.views import page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'digitaltpersonvern.views.home', name='home'),
    # url(r'^digitaltpersonvern/', include('digitaltpersonvern.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^n/', include('samklang_blog.urls')),
    #url(r'^$', IndexView.as_view()),
    url(r'^$', page, kwargs={'url': '/om/'}),
)

if settings.DEVELOPMENT_MODE:
    import os

    urlpatterns += patterns('',
            (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
            )

