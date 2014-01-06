from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'citizens_services.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^citizens/', include('citizens.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
