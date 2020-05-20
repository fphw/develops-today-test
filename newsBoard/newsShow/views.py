from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import TemplateView
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from news.models import Article

# Create your views here.


class Home(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        ctx = {}
        all_articles = Article.objects.all()
        count_comments = Article.objects.annotate(
            number_of_answers=Count('commentArticle'))
        ctx['articles'] = zip(all_articles, count_comments)
        return render(request, self.template_name, ctx)


def addLike(request, id):
    try:
        article = Article.objects.get(pk=id)
        article.likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')
