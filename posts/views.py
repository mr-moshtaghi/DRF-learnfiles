from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Posts
from .serializers import PostsSerializers

# Create your views here.


class ListPosts(ListAPIView):
    serializer_class = PostsSerializers
    queryset = Posts.objects.all()