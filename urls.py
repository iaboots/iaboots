from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iaboots.views.home', name='home'),
    # url(r'^iaboots/', include('iaboots.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^ask$', 'chat.views.ask', name='ask'),
    url(r'^/?$', 'chat.views.home', name='home'),
    url(r'^interact?$', 'chat.views.interact', name='interact'),
    url(r'^entrar?$', 'chat.views.entrar', name='entrar'),
)
