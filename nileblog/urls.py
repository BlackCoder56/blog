from . import views
from django.urls import path

urlpatterns = [
    path("", views.baseView.as_view()),
]
