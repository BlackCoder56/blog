from django.shortcuts import render, get_object_or_404
from django.views import generic
from nileblog.models import Article, Like
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.generic.dates import ArchiveIndexView

# Create your views here.
class ArticleArchiveIndexView(ArchiveIndexView):
    queryset = Article.objects.filter(pub_date__lte=timezone.now())
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
    
    # def get_queryset(self):
    #     return Article.objects.filter(pub_date__lte=timezone.now())

class DetailView(generic.DetailView):
    model = Article
    template_name = "nileblog/article_detail.html"
    
    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=timezone.now())

def Likes(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    
def upvote(request):
    pass

def downvote(request):
    pass