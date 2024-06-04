from django.shortcuts import render, HttpResponse
from django.views import generic
from nileblog.models import Article

# Create your views here.
class indexView(generic.ListView):
    model = Article
    template_name = "nileblog/article_list.html"
    