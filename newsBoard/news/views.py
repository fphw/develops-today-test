from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import get_object_or_404
# Create your views here.
from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentListSerializer
from rest_framework.permissions import AllowAny

# class ArticleApiView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({"articles": serializer.data})

#     def post(self, request):
#         articles = request.data.get('article')

#         serializer = ArticleSerializer(data=articles)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({"success": "Article '{}' created successfully"
#                          .format(article_saved.title)})

#     def put(self, request, pk):
#         saved_article = get_object_or_404(Article.objects.all(), pk=pk)
#         data = request.data.get('article')
#         serializer = ArticleSerializer(instance=saved_article, data=data,
#                                        partial=True)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({"success": "Article '{}' updated successfully"
#                          .format(article_saved.title)})

#     def delete(self, request, pk):
#         articel = get_object_or_404(Article.objects.all(), pk=pk)
#         articel.delete()
#         return Response({
#             "message": "Article with id `{}` has been deleted.".format(pk)
#         })


class ArticleCreateApiView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ArticleListSerializer


class ArticleListApiView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()


class ArticleUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()


class CommentListApiView(generics.ListAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()


class CommentCreateApiView(generics.CreateAPIView):
    serializer_class = CommentListSerializer


class CommentUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()
