from django.contrib.syndication.views import Feed
from samklang_blog.models import Entry

class LatestEntriesFeed(Feed):
    title = "Siste nytt fra Digitalt Personvern"
    link = "/"

    def items(self):
        return Entry.live.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body_html

    def item_pubdate(self, item):
        return item.pub_date

    def item_author_name(self, item):
        name = item.user.get_full_name()
        if not name:
            name = item.user.username
        return name
