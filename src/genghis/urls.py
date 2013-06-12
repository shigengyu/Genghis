from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^article/', include('article.urls')),
    url(r'^photos/', include('photos.urls')),
    url(r'^files/', include('files.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^profile/', include('about.urls')),
    url(r'^socialauth/', include('social_auth.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
