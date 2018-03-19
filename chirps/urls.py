from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import *

urlpatterns = [

    # using the views that I wrote
    # path('', chirp_list_view, name='list'),
    # path('1', chirp_detail_view, name='list')

    # using the pre-made django views
    path('', ChirpListView.as_view(), name='list'), # /chirp/
    re_path(r'(?P<pk>\d+)/', ChirpDetailView.as_view(), name='detail') # /chirp/id/
]
