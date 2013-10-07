from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testBlog.views.home', name='home'),
    # url(r'^testBlog/', include('testBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'blog.views.index'),
	url(r'^search-form/', 'blog.views.search_form'),
	url(r'^search/', 'blog.views.search_form'),

	url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),

)
