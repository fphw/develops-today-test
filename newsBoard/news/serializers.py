from rest_framework import serializers
from .models import Article, Comment, Author


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=80)
#     link = serializers.URLField(max_length=200)
#     creation_date = serializers.DateTimeField(read_only=True)
#     likes = serializers.IntegerField(required=False)
#     author_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.link = validated_data.get('link', instance.link)
#         instance.creation_date = validated_data.get(
#             'creation_date', instance.creation_date)
#         instance.likes = validated_data.get('likes', instance.likes)
#         instance.author_id = validated_data.get(
#             'author_id', instance.author_id)

#         instance.save()
#         return instance


class ArticleListSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateTimeField()

    class Meta:
        model = Article
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateTimeField()
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    article = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1
