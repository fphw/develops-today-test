from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import TemplateView
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from news.models import Article, Comment
from .form import CommentAddForm

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


def showComments(request):
    ctx = {}
    try:
        comments = Comment.objects.all()
        ctx['comments'] = comments
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'comments.html', ctx)


class AddCommentFormView(TemplateView):
    add_comment_form = CommentAddForm

    def post(self, request, id):
        comments = Comment.objects.all().filter(article=id)
        ctx['comments'] = comments
        form = CommentAddForm(request.POST)
        ctx = {
            'add_comment': form,
            'id': id,
        }
        if form.is_valid():
            data = form.cleaned_data
            form.save(commit=False)
            form.article_id = 'Some articel 1'
            form.save()
            # return render(request, 'comments.html', ctx)
            return HttpResponse(form.cleaned_data.items())
        else:
            print('Form:', form)
            return render(request, 'comments.html', ctx)

    def get(self, request, id):
        try:
            ctx = {}
            comments = Comment.objects.all().filter(article=id)
            ctx['comments'] = comments
            ctx['add_comment'] = self.add_comment_form
            ctx['id'] = id
            return render(request, 'comments.html', ctx)
        except ObjectDoesNotExist:
            raise Http404
