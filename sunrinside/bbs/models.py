from django.db import models
from django.contrib import auth
from django.utils import timezone

class Board(models.Model):
  creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  created_date = models.DateTimeField(default=timezone.now)
  def __str__(self):
      return self.title
  
class Article(models.Model):
  author = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
  board = models.ForeignKey(Board, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=1000)
  created_date = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return self.title

class Comment(models.Model):
  author = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  text = models.CharField(max_length=200)
  created_date = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return self.text