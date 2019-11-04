from django.contrib.syndication.views import Feed
from django.urls import reverse
from jobs.models import Jobs

class LatestEntriesFeed(Feed):
    title = "iWantRemote: Remote Tech Jobs"
    link = "/feed/"
    description = "Updates on changes and additions to job feed."
    language="en"

    def items(self):
        return Jobs.objects.order_by('-create_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_applylink(self, item):
        return item.link

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def jobfeed(self, item):
        return reverse('job-feed', args=[item.pk])