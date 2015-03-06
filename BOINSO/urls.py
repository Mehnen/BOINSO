from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('api.urls')),
    # Examples:
    # url(r'^$', 'BOINSO.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
