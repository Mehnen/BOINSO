from django.conf.urls import patterns, url
from api.views import api_root, UserList, UserDetail

urlpatterns = patterns(
    '',
    url(r'^$', api_root),
    url(r'^users/$',
        UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        UserDetail.as_view(),
        name='user-detail')
)
