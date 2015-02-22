from django.conf.urls import patterns, include, url
from django.contrib import admin
from disclosures.views import index, search, faq

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^search$', search, name='search'),

    url('^faq$', faq, name='faq'),
    url('^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
