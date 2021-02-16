from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Article
        fields = ['title', 'slug', 'body', 'thumb', 'username']

    def get_username_from_author(self, blog_post):
        username = blog_post.author.username
        return username
