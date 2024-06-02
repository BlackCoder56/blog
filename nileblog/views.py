from django.shortcuts import render, HttpResponse
from django.views import generic
from nileblog.models import Article

# Create your views here.
class baseView(generic.ListView):
    model = Article
    template_name = "nileblog/base.html"
    