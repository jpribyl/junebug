from django.urls import path, re_path
from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import *

urlpatterns = [

    # using the views that I wrote
    # path('', chirp_list_view, name='list'),
    # path('1', chirp_detail_view, name='list')

    # using the pre-made django views
    path('', RedirectView.as_view(url='/')), # /chirp/search
    path('search/', ChirpListView.as_view(), name='list'), # /chirp/search
    path('create/', ChirpCreateView.as_view(), name='create'), # /chirp/create/

    # children need to be higher than parents
    re_path(r'(?P<pk>\d+)/update', ChirpUpdateView.as_view(), name='update'), # /chirp/id/update/
    re_path(r'(?P<pk>\d+)/delete', ChirpDeleteView.as_view(), name='delete'), # /chirp/id/delete/
    re_path(r'(?P<pk>\d+)/', ChirpDetailView.as_view(), name='detail'), # /chirp/id/
]
