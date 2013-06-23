from django.conf.urls import patterns, include, url, static
from django.conf import settings
from genghis.views import WikiRedirectView, MySqlRedirectView
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^photos/', include('photos.urls')),
    url(r'^files/', include('files.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^profile/', include('about.urls')),
    url(r'^socialauth/', include('social_auth.urls')),
    url(r'^wiki/', WikiRedirectView.as_view()),
    url(r'^mysql/', MySqlRedirectView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)


'''
named_patterns = {
    url(r'^$', include('home.urls')): 'Home',
    url(r'^home/', include('home.urls')): 'Home',
    url(r'^articles/', include('articles.urls')): 'Articles',
    url(r'^photos/', include('photos.urls')): 'Photos',
    url(r'^files/', include('files.urls')): 'Files',
    url(r'^about/', include('about.urls')): 'About',
    url(r'^profile/', include('about.urls')): 'Profile',
    url(r'^socialauth/', include('social_auth.urls')): 'Social Authentication',
    url(r'^wiki/', WikiRedirectView.as_view()): '',
    url(r'^mysql/', MySqlRedirectView.as_view()): '',
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
}

list = []
list.append('')
for item in named_patterns.keys():
    list.append(item)
urlpatterns = patterns(list)
'''