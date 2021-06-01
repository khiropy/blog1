from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

class Post(models.Model):
    title = models.TextField(max_length=20)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])



# Create your models here.
