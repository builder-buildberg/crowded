from django.contrib.sitemaps import Sitemap as DjangoSitemap
from django.urls import reverse
from ground.views import GroundListView
from ground.models import Ground  # Replace this with the actual model used in GroundListView

class Sitemap(DjangoSitemap):
    protocol = 'https'
    domain = 'crowded.pk'
    priority = 0.5
    changefreq = 'daily'

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    protocol = 'https'
    domain = 'crowded.pk'
    def items(self):
        return ['home', 'go']

    def location(self, item):
        return reverse(item)
    
class GroundSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    protocol = 'https'
    domain = 'crowded.pk'
    def items(self):
        return Ground.objects.all()  # Replace Ground with the actual model used in GroundListView

    def location(self, obj):
        return reverse('ground_detail', args=[obj.slug])