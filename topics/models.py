from django.db import models
from django.conf import settings

import markdown

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField(max_length=100)
    posted = models.DateField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text


class Topic(models.Model):
    heading = models.CharField(max_length=30)
    text = models.TextField()
    posted = models.DateField(auto_now=True)
    tags = models.ManyToManyField(
        Tag,
        related_name="topics"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="topics"
    )
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.heading


class Answer(models.Model):
    text = models.TextField()
    posted = models.DateField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    def __str__(self):
        return self.text
