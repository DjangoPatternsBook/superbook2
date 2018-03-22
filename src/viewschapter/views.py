from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView
from django.core.exceptions import PermissionDenied
from datetime import datetime
from posts import models


def hello_fn(request, name="World"):
    return HttpResponse("Hello {}!".format(name))


class HelloView(View):

    def get(self, request, name="World"):
        return HttpResponse("Hello {}!".format(name))


class GreetView(View):
    greeting = "Hello {}!"
    default_name = "World"

    def get(self, request, **kwargs):
        name = kwargs.pop("name", self.default_name)
        return HttpResponse(self.greeting.format(name))


class SuperVillainView(GreetView):
    greeting = "We are the future, {}. Not them. "
    default_name = "my friend"


class FeedMixin(object):
    feed_context_name = "feed"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.feed_context_name] = models.Post.objects.viewable_posts(
            self.request.user)
        return context


class LoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class MyFeed(LoginRequiredMixin, FeedMixin, TemplateView):
    template_name = "myfeed.html"


class PublicPostJSONView(View):

    def get(self, request, *args, **kwargs):
        msgs = models.Post.objects.public_posts().values(
            "posted_by_id", "message")[:5]
        return JsonResponse(list(msgs), safe=False)


class YearView(View):

    def get(self, request, year):
        try:
            d = datetime(year=year, month=1, day=1)
            reply = "First day of the year {} is {}!".format(
                year, d.ctime())
        except ValueError:
            reply = "Error: Invalid year!"
        return HttpResponse(reply)


class BlogHomeView(TemplateView):
    template_name = "blog_home.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ArticleView(TemplateView):
    template_name = "article.html"
