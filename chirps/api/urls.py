from django.urls import path, re_path
from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import *


urlpatterns = [
    path('create/', ChirpCreateAPIView.as_view(), name='api-create'),
    path('', ChirpListAPIView.as_view(), name='api-list')
]
