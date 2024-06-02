from django.db import models

# Create your models here.
class Article(models.Model):
    title_text = models.CharField(max_length=50)
    preview_text = models.CharField(max_length=100)
    details_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.title_text
    
class Like(models.Model):
    title_text = models.ForeignKey(Article, on_delete=models.CASCADE)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    
    
class Commnt(models.Model):
    title_text = models.ForeignKey(Article,  on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=1000)
