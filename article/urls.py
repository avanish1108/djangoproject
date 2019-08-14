from django.urls import path
from .views import ArticleView
app_name="article"
urlpatterns = [
    path('article/',ArticleView.as_view()),
    path('article/<int:pk>',ArticleView.as_view()),
]