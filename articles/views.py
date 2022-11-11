from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required  

# Create your views here.


def index(request):

    articles = Article.objects.order_by('-pk')
    comments = Comment.objects.order_by('-pk')

    page = request.GET.get('page', '1')
    paginator = Paginator(articles, 5)
    paginated_articles = paginator.get_page(page)
    max_index = len(paginator.page_range)

    c_paginator = Paginator(comments, 3)
    paginated_comments = c_paginator.get_page(page)
    c_max_index = len(c_paginator.page_range)

    context = {
        "articles": articles,
        "paginated_articles": paginated_articles,
        "max_index": max_index,
        "comments": comments,
        "paginated_comments": paginated_comments,
        "c_max_index": c_max_index,
    }

    return render(request, 'articles/index.html', context)

@login_required
def create(request):

    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/create.html", context)

def detail(request, pk):

    return render(request, "articles/detail.html")

@login_required
def delete(request, pk):

    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect("articles:index")

@login_required
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


@login_required
def c_create(request, pk):

    comment = request.POST.get("comment")
    article = Article.objects.get(pk=pk)


    if comment != "":
        Comment.objects.create(content=comment, article=article, user=request.user)

    return redirect("articles:index")

@login_required
def c_delete(request, pk):

    comment = Comment.objects.get(pk=pk)
    comment.delete()

    return redirect("articles:index")

@login_required
def like(request, pk):

    article = Article.objects.get(pk=pk)

    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)

    return redirect('articles:index')

    