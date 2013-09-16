from django.conf.urls import patterns, include, url
from testsite.views import hello, current_datetime, hours_ahead

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^testsite/', include('testsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    # use d+ to match one or more digits
    #url(r'^time/plus/\d+/$', hours_ahead),
    # use parentheses around the value to save it.
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
