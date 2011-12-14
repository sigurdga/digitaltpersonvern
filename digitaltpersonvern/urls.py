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
    (r'^ut/', 'django.contrib.auth.views.logout', {'next_page': '/'}, 'auth_logout'),
    (r'^inn/', 'django.contrib.auth.views.login', {}, 'auth_login'),
    url(r'^menu/', include('samklang_menu.urls')),
    url(r'^files/', include('samklang_media.urls')),
    url(r'^pages/', include('samklang_pages.urls')),
    #(r'^u/', include('registration.urls')),
    url(r'^blog/', include('samklang_blog.urls')),
    url(r'^donate/', include('samklang_payment.urls')),
    #url(r'^$', IndexView.as_view()),
    url(r'^$', page, kwargs={'url': '/om/'}),
)

if settings.DEVELOPMENT_MODE:
    import os

    urlpatterns += patterns('',
            (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
            )

