from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('batteryLevel.views',

    url(r'^level$', 'level'),

)
