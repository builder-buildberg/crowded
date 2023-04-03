from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from ground.models import Ground
from ground.views import GroundListView


class StaticViewSitemap(Sitemap):
    protocol = 'https'
    priority = 0.5
    changefreq = 'monthly'
    def items(self):
        return ['home', 'ground_list', 'go']
    

    def location(self, item):
        return reverse(item)
    
class GroundSitemap(Sitemap):
    protocol = 'https'
    priority = 0.5
    changefreq = 'weekly'
    def items(self):
        return Ground.objects.all()
    

    def location(self, obj):
        return reverse('ground_detail', args=[obj.slug])