from django.conf.urls import patterns, include, url
from django.contrib import admin
from disclosures.views import index

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    # url(r'^blog/', include('blog.urls')),

    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
