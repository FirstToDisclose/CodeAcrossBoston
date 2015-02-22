from django.conf.urls import patterns, include, url
from django.contrib import admin
from disclosures.views import index, search, faq

from disclosures.views import agreements
from disclosures.views import disclosure
from disclosures.views import search
from disclosures.views import tag
from disclosures.views import show_disclosure


urlpatterns = patterns('',
    url(r'^$', index),

    url(r'^search$', search, name='search'),
    url(r'^disclosure/(?P<pk>\d+)$', show_disclosure, name='disclose'),

    url('^faq$', faq, name='faq'),
    url('^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^agreements/', agreements, name='agreements'),
    url(r'^disclosure/', disclosure, name='disclosure'),
    url(r'^tag/', tag, name='tag'),

    url('^accounts/', include('django.contrib.auth.urls')),
    url('', include('social.apps.django_app.urls', namespace='social'))

)
