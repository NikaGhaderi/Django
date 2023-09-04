from django.contrib import admin
from django.urls import path
from .views import (
    articleListView,
    articleDetailView,
    articleCreateView,
    articleUpdateView,
    articleDeleteView
)

app_name = 'articles'
urlpatterns = [
    path('', articleListView.as_view(), name='article-list'),
    path('<int:id>/', articleDetailView.as_view(), name='article-detail'),
    path('create/', articleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', articleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', articleDeleteView.as_view(), name='article-delete'),
]