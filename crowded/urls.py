"""crowded URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ground.views import GroundListView
import ground.views as gv
from django.conf import settings  # new
from django.urls import path  # new
from django.conf.urls.static import static  # new

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.sitemaps.views import sitemap
from ground.sitemaps import StaticViewSitemap, GroundSitemap , Sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'ground': GroundSitemap,
    'sitemap': Sitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gv.home, name='home'),
    path('ground', GroundListView.as_view(), name='ground_list'),
    path('ground/<slug:slug>', gv.GroundDetailView.as_view(), name='ground_detail'),
    path('go', gv.go, name='go'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)