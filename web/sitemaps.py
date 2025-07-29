from django.contrib.sitemaps import Sitemap
from .models import Post, Work
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'solutions', 'works', 'contacts']

    def location(self, item):
        return reverse(item)

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()

class WorkSitemap(Sitemap):
    def items(self):
        return Work.objects.all()
