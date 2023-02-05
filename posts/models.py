from django.contrib.auth.models import AbstractUser
from django.db import models
from tinymce.models import HTMLField
from django.db import models


class User(AbstractUser):
    """
    Extend the user object to add the job_description
    field
    """

    job_description = models.CharField(max_length=100, blank=True, null=True)
   
class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    summary = models.TextField(max_length=400, blank=True, null=True)
    content = HTMLField(blank=True, null=True)
    published = models.BooleanField(default=False)
    date_published = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
