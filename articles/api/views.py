from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from articles.models import Article
from articles.api.serializers import ArticleSerializer


@api_view(['GET'])
def api_view(request, slug):

    try:
        blog_post = Article.objects.get(slug=slug)
    except Article.donotexist:
        return Response(status=status.http_404_not_found)

    if request.method == 'GET':
        serializer = ArticleSerializer(blog_post)
        return Response(serializer.data)