from django.contrib.sitemaps import Sitemap as DjangoSitemap
from django.urls import reverse
from ground.views import GroundListView
from ground.models import Ground  # Replace this with the actual model used in GroundListView

class Sitemap(DjangoSitemap):
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> parent of cb3fde4 (🎉)
    def get_urls(self, page=1, site=None, protocol=None):
        urls = super().get_urls(page, site, protocol)
        for url in urls:
            url['changefreq'] = 'weekly'
            url['priority'] = 0.5
        return urls
<<<<<<< HEAD
=======
=======
    protocol = 'https'
    domain = 'crowded.pk'
    priority = 0.5
    changefreq = 'daily'
>>>>>>> parent of f4fcb2e (🎉)
>>>>>>> parent of cb3fde4 (🎉)

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