from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

from views import IndexView
from feeds import LatestEntriesFeed

from samklang_pages.views import page

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inn/', 'django.contrib.auth.views.login', name='login'),
    url(r'^ut/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^passord/bytt/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^passord/bytt/ferdig/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^passord/nullstill/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^passord/nullstill/ferdig/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^nullstill/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^nullstill/ferdig/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^meny/', include('samklang_menu.urls')),
    url(r'^filer/', include('samklang_media.urls')),
    url(r'^sider/', include('samklang_pages.urls')),
    #(r'^u/', include('registration.urls')),
    url(r'^blogg/', include('samklang_blog.urls')),
    url(r'^donate/', include('samklang_payment.urls')),
    #url(r'^$', IndexView.as_view()),
    url(r'^$', page, kwargs={'url': '/'}),

    # feeds
    url(r'^feed/blogg/$', LatestEntriesFeed()),
)

if settings.DEVELOPMENT_MODE:
    import os

    urlpatterns += patterns('',
            (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
            )

