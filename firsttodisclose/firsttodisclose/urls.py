from django.conf.urls import patterns, include, url
from django.contrib import admin
from disclosures.views import index, search

from disclosures.views import agreements
from disclosures.views import disclosure
from disclosures.views import search
from disclosures.views import tag

urlpatterns = patterns('',
    url(r'^$', index),

    url(r'^search$', search),
    # url(r'^blog/', include('blog.urls')),

    url('^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^agreements/', agreements),
    url(r'^disclosure/', disclosure),
    url(r'^search/', search),
    url(r'^tag/', tag),

    url('^accounts/', include('django.contrib.auth.urls')),
    url('', include('social.apps.django_app.urls', namespace='social'))

)
