from django.shortcuts import render, HttpResponse
from django.views import generic
from nileblog.models import Article, Like
from django.utils import timezone

# Create your views here.
class indexView(generic.ListView):
    template_name = "nileblog/article_list.html"
    context_object_name = "article_list"
    
    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
   
    
def upvote(request):
    pass

def downvote(request):
    pass