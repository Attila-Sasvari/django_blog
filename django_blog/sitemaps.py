from django.contrib.sitemaps import Sitemap
from blog.models import Blog


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Blog.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at
