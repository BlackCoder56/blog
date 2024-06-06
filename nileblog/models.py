import datetime
from django.utils import timezone
from django.db import models


# Create your models here.
class Article(models.Model):
    title_text = models.CharField(max_length=50)
    preview_text = models.CharField(max_length=200)
    details_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField("date published")
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def __str__(self):
        return self.title_text
    
class Like(models.Model):
    title_text = models.ForeignKey(Article, on_delete=models.CASCADE)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    
    
class Comment(models.Model):
    title_text = models.ForeignKey(Article,  on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=1000)
