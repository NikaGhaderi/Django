from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from .models import Article
from .forms import modelForm


class articleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # It looks for this template automatically: blog/<model name>_list.html


class articleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = modelForm
    queryset = Article.objects.all()

    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self)
    #   return '/'


class articleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = modelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class articleDetailView(DetailView):
    # primary lookup: pk pr slug. pk is also known as the id field, so id = pk, but it stands for primary key.
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):  # built-in function.
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class articleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("articles:article-list")