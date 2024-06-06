from django.shortcuts import render, HttpResponse
from django.views import generic
from nileblog.models import Article

# Create your views here.
class indexView(generic.ListView):
    template_name = "nileblog/article_list.html"
    context_object_name = "article_list"
    
    def get_queryset(self):
        return Article.objects.all()