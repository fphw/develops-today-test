from django.forms import ModelForm
from django.forms import HiddenInput
from news.models import Article, Comment


class CommentAddForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        #widgets = {'article': HiddenInput()}
