# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView, post_new, post_delete, post_edit, post_image_new, post_image_edit
from django.conf import settings
from django.conf.urls.static import static

post_list = PostView.as_view({
    'post': 'create',
    'get': 'list'
})
post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('post_new/', post_new, name='post_new'),
    path('post_image_new/', post_image_new, name='post_image_new'),
    path('post_del/', post_delete, name='post_delete'),
    path('post_edit/', post_edit, name='post_edit'),
    path('post_image_edit/', post_image_edit, name='post_image_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)