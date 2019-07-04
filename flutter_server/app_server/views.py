# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions
from django.http import HttpResponse
from .form import PostForm
from django.utils import timezone
from dateutil.parser import parse


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()


def post_new(request):
    if request.method == "POST":
        try:
            post = Post()
            post.user_id = request.POST['user_id']
            post.content = request.POST['content']
            post.title = request.POST['title']
            tmp_time = timezone.now()
            dt_parser = parse(str(tmp_time))
            post.created_at = dt_parser.date()
            post.save()
            return HttpResponse('성공')
        except:
            return HttpResponse('실패')


def post_image_new(request):
    if request.method == "POST":
        tmp = 0
        try:
            post = Post()
            post.user_id = request.POST['user_id']
            post.content = request.POST['content']
            post.title = request.POST['title']
            tmp_time = timezone.now()
            dt_parser = parse(str(tmp_time))
            post.created_at = dt_parser.date()
            if request.FILES['image'] is not None:
                post.image = request.FILES['image']
            post.save()
            return HttpResponse('성공')
        except:
            return HttpResponse('실패')


def post_edit(request):
    if request.method == "POST":
        try:
            post = Post.objects.get(id=int(request.POST['id']))
            post.id = request.POST['id']
            post.user_id = request.POST['user_id']
            post.content = request.POST['content']
            post.title = request.POST['title']
            post.save()
            return HttpResponse('성공')
        except:
            post = None
            return HttpResponse('실패')

def post_image_edit(request):
    if request.method == "POST":
        try:
            post = Post.objects.get(id=int(request.POST['id']))
            post.id = request.POST['id']
            post.user_id = request.POST['user_id']
            post.content = request.POST['content']
            post.title = request.POST['title']
            post.image = request.FILES['image']
            post.save()
            return HttpResponse('성공')
        except:
            post = None
            return HttpResponse('실패')


def post_delete(request):
    try:
        post = Post.objects.get(id=int(request.POST['id']))
        post.delete()
        return HttpResponse('성공')
    except:
        return HttpResponse('실패')