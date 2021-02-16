from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from articles.models import Article
from articles.api.serializers import ArticleSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def api_detail_view(request, slug):

    try:
        blog_post = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(blog_post)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def api_update_view(request, slug):
    try:
        blog_post = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response':"You don't have permission to edit."})

    if request.method == 'PUT':
        serializer = ArticleSerializer(blog_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update successfuly'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def api_delete_view(request, slug):

    try:
        blog_post = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response':"You don't have permission to delete."})


    if request.method == "DELETE":
        operation = blog_post.delete()
        data = {}
        if operation:
            data['success'] = "delete succsessful"
        else:
            data['failure'] = "delete failed"
        return Response(data=data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def api_create_view(request):
    account = request.user
    blog_post = Article(author=account)
    if request.method == 'POST':
        serializer = ArticleSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
