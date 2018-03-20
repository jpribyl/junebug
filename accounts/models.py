from django.conf.urls import url
from django.urls import path, re_path
from django.views.generic.base import RedirectView

from .views import (
    UserDetailView
    )


urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")), 
    # url(r'^search/$', ChirpListView.as_view(), name='list'), # /chirp/
    # url(r'^create/$', ChirpCreateView.as_view(), name='create'), # /chirp/create/
    re_path(r'(?P<username>[\w.@+-]+)/', UserDetailView.as_view(), name='detail'), # /chirp/id/update/
    # url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'), # /chirp/1/
    # url(r'^(?P<pk>\d+)/update/$', ChirpUpdateView.as_view(), name='update'), # /chirp/1/update/
    # url(r'^(?P<pk>\d+)/delete/$', ChirpDeleteView.as_view(), name='delete'), # /chirp/1/delete/
]
