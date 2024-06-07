from nileblog.views import ArticleArchiveIndexView, DetailView
from django.urls import path

app_name = "nileblog"

urlpatterns = [
    path("", ArticleArchiveIndexView.as_view(), name="article_index_archive"),
    path("<int:pk>/detail", DetailView.as_view(), name="detail"),
]
