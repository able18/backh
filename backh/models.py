from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True)
    end_date = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class Donor(models.Model):
    firstname = models.CharField(max_length=200, blank=True)
    lastname = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    amount = models.IntegerField()
    message = models.TextField(max_length=500, null=True
                               , blank=True)

    def __str__(self):
        return self.firstname


class Photo(models.Model):
    photo = models.ImageField(upload_to='nimage/', blank=True, null=True)


# upload_to='photos/',

class Post(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
