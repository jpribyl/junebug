"""junebug URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from .views import home
from chirps.views import ChirpListView

urlpatterns = [
    path('admin/', admin.site.urls), # /admin
    path('', ChirpListView.as_view(), name='home'), # /

    # include the accounts app
    path('profiles', include('accounts.urls')), # /chirp/

    # include the chirps app
    path('chirp/', include('chirps.urls')), # /chirp/
    path('api/chirp/', include('chirps.api.urls')), # /api/chirp/
]

if settings.DEBUG:
    urlpatterns += (static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT))
