from django.db import models
# from django.contrib.auth import get_user_model
# User = get_user_model()


class Author(models.Model):
    class Meta:
        db_table = 'author'

    name = models.CharField(verbose_name='Author', max_length=40)
    email = models.EmailField(verbose_name='E-mail')

    def __str__(self):
        return self.name


class Article(models.Model):
    class Meta:
        db_table = 'article'

    title = models.CharField(verbose_name='Title', max_length=80, blank=False)
    link = models.URLField(verbose_name='Link', max_length=200, blank=False)
    creation_date = models.DateTimeField(
        verbose_name='Creation date', auto_now_add=True, auto_now=False)
    author = models.ForeignKey(
        Author, verbose_name='Author', related_name='articles', on_delete=models.CASCADE)
    likes = models.IntegerField(blank=True, default=0, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    author = models.ForeignKey(
        Author, verbose_name='Author', related_name='commentAuthor', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Content', max_length=1000)
    creation_date = models.DateTimeField(
        verbose_name='Creation date', auto_now_add=True, auto_now=False)
    article = models.ForeignKey(Article, verbose_name='Article',
                                related_name='commentArticle', on_delete=models.CASCADE)
