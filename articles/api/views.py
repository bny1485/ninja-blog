from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.api.serializers import ArticleSerializer


@api_view(['GET'])
def api_detail_view(request, slug):

    try:
        blog_post = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status=status.http_404_not_found)

    if request.method == 'GET':
        serializer = ArticleSerializer(blog_post)
        return Response(serializer.data)


@api_view(['PUT'])
def api_update_view(request, slug):
    try:
        blog_post = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status=status.http_404_not_found)

    if request.method == 'PUT':
        serializer = ArticleSerializer(blog_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update successfuly'
            return Response(data=data)
        return Response(serializer.errors, status=status.http_400_bad_request)


@api_view(['DELETE'])
def api_delete_view(request, slug):

    try:
        blog_post = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status=status.http_404_not_found)

    if request.method == 'DELETE':
        operation = blog_post.delete()
        data = {}
        if operation:
            data['success'] = "delete succsessful"
        else:
            data['failure'] = "delete failed"
        return Response(data=data)


@api_view(['POST'])
def api_create_view(request):
    accounts = user.objects.get(pk=1)
    blog_post = Article(author=account)
    if requeset.method == 'POST':
        serializer = ArticleSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.http_201_CREATED)
        return Response(serializer.errors, status=status.http_400_bad_request)
