# -*- coding: utf-8 -*-
from django.db import models


class Post(models.Model):
    user_id = models.CharField(max_length=144)
    title = models.CharField(max_length=144)
    content = models.TextField()
    created_at = models.CharField(max_length=144)
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/img')

    def __str__(self):
        return self.title
