from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed
from blog.models import Blog


class LatestPostsFeed(Feed):
    title = "My blog"
    link = ""
    description = "New articles of my blog."

    def items(self):
        return Blog.objects.filter(is_published=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.lead, 30)


class atomFeed(Feed):
    feed_type = Atom1Feed
