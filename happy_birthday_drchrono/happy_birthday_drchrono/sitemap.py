from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return [
            'home',
        ]

    def location(self, item):
        return reverse(item)
