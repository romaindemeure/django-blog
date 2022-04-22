from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import BlogPost
from posts.serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (IsAuthenticated,)
