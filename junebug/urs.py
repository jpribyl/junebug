from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import chirp_detail_view, chirp_list_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', chirp_list_view, name='list'),
    path('1', chirp_detail_view, name='list')
]
