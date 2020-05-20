from django.urls import path, include
#from .views import ArticleApiView
from .views import ArticleCreateApiView, ArticleListApiView, \
    ArticleUpdateApiView, CommentListApiView, CommentCreateApiView, \
    CommentUpdateApiView

app_name = "news"

urlpatterns = [
    # path('articles/', ArticleApiView.as_view()),
    # path('articles/<int:pk>', ArticleApiView.as_view()),
    path('articles/create/', ArticleCreateApiView.as_view()),
    path('articles/', ArticleListApiView.as_view()),
    path('articles/update/<int:pk>', ArticleUpdateApiView.as_view()),
    path('comments/', CommentListApiView.as_view()),
    path('comments/create', CommentCreateApiView.as_view()),
    path('comments/update/<int:pk>', CommentUpdateApiView.as_view()),
]
