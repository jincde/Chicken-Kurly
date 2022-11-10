from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.


def index(request):

    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

def create(request):

    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/create.html", context)

def detail(request, pk):

    return render(request, "articles/detail.html")


def delete(request, pk):

    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect("articles:index")


def update(request, pk):

    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/update.html", context)