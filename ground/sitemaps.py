from django.contrib.sitemaps import Sitemap as DjangoSitemap
from django.urls import reverse
from ground.views import GroundListView
from ground.models import Ground  # Replace this with the actual model used in GroundListView

class Sitemap(DjangoSitemap):
    protocol = 'https'
    changefreq = 'weekly'
    priority = 0.9

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'go']

    def location(self, item):
        return reverse(item)
    
class GroundSitemap(Sitemap):
    def items(self):
        return Ground.objects.all()  # Replace Ground with the actual model used in GroundListView

    def location(self, obj):
        return reverse('ground_detail', args=[obj.slug])