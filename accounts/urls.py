from django.conf.urls import url
from django.urls import path, re_path

from django.views.generic.base import RedirectView

from .views import *

urlpatterns = [
    # url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'), # /tweet/1/
    re_path(
        r'(?P<username>[\w.@+-]+)/', 
        UserDetailView.as_view(), 
        name='profiles-detail'), # /chirp/id/update/
]
