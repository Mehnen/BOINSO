from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns(
    '',
    url(r'^$', views.api_root),
    url(r'^sign_up/$',
        views.SignUp.as_view(),
        name='sign-up'),
    url(r'^login/$',
        views.Login.as_view(),
        name='login'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^user-profiles/$',
        views.UserProfileProxy.as_view(),
        name='user-profile-proxy'),
    url(r'^user-profiles/(?P<pk>[0-9]+)/$',
        views.UserProfileDetail.as_view(),
        name='userprofile-detail'),
    url(r'^satellites/$',
        views.SatelliteList.as_view(),
        name='satellite-list'),
    url(r'^satellites/(?P<pk>[0-9]+)/$',
        views.SatelliteDetail.as_view(),
        name='satellite-detail'),
    url(r'^transponders/(?P<pk>[0-9]+)/$',
        views.TransponderDetail.as_view(),
        name='transponder-detail')
)
