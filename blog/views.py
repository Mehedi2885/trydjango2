from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article
from .forms import ArticleModelForms


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForms
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # form = ArticleModelForms(Article, )


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    # queryset = Article.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForms
   # queryset = Article.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # form = ArticleModelForms(Article, )


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    # queryset = Article.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("articles:article-list")

