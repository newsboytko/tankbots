from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'tankbots.views.home', name='home'),
    url(r'^game/', include('game.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
