from django.conf.urls import patterns, include, url
from django.contrib import admin

from MobileDeviceInfoMonitor import views


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^battery$', views.battery),

    url(r'^batteryLevel/', include('batteryLevel.urls')),
)
