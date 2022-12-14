from django.shortcuts import render, redirect
from .forms import ArticleForm, ReCommentForm
from .models import Article, Comment, ReComment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required  
from django.http import JsonResponse
from products.models import Product
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def index(request):

    articles = Article.objects.order_by('-pk')
    comments = Comment.objects.order_by('-pk')

    page = request.GET.get('page', '1')
    paginator = Paginator(articles, 9)
    paginated_articles = paginator.get_page(page)
    max_index = len(paginator.page_range)


    context = {
        "articles": articles,
        "paginated_articles": paginated_articles,
        "max_index": max_index,
        "comments": comments,
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

@login_required
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article).order_by('-pk')
    recomment_form = ReCommentForm()
    recomments = ReComment.objects.all().order_by('-pk')

    page = request.GET.get('page', '1')
    paginator = Paginator(comments, 5)
    paginated_comments = paginator.get_page(page)
    max_index = len(paginator.page_range)

    context = {
        'article': article,
        'comments': comments,
        'recomment_form': recomment_form,
        'paginated_comments': paginated_comments,
        'max_index': max_index,
        'recomments': recomments,
    }

    return render(request, "articles/detail.html", context)

def rec_detail(request, c_pk, a_pk):

    article = Article.objects.get(pk=a_pk)
    comment = Comment.objects.get(pk=c_pk)
    recomments = ReComment.objects.filter(comment=comment).order_by('-pk')
    recomment_form = ReCommentForm()

    # ????????? ??????????????????
    recomment_page = request.GET.get('recomment_page', '1')
    recomment_paginator = Paginator(recomments, 5)
    recomment_page_obj = recomment_paginator.get_page(recomment_page)

    # page = request.GET.get('page', '1')
    # paginator = Paginator(recomments, 5)
    # paginated_recomments = paginator.get_page(page)
    # max_index = len(paginator.page_range)

    context = {
        'comment': comment,
        'recomments': recomments,
        'recomments': recomment_page_obj,
        # 'paginated_recomments': paginated_recomments,
        'recomment_form': recomment_form,
        # 'max_index': max_index,
        'article': article,
    }

    return render(request, 'articles/recomment.html', context)

@login_required
def delete(request, pk):

    article = Article.objects.get(pk=pk)

    if request.user == article.user:
        article.delete()
    return redirect("articles:index")

@login_required
def update(request, pk):

    article = Article.objects.get(pk=pk)

    if request.user == article.user:
        if request.method == "POST":
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                article_form.save()
                return redirect("articles:index")
        else:
            article_form = ArticleForm(instance=article)
        context = {
            "article_form": article_form,
            "article": article,
        }
        return render(request, "articles/update.html", context)
    return redirect("articles:index")


@login_required
def c_create(request,pk):

    comment = request.POST.get("comment")
    article = Article.objects.get(pk=pk)

    Comment.objects.create(content=comment, article=article, user=request.user)
    
    # ?????? ???????????? ?????? ??????
    # context = {
    #     'content': comment,
    #     'userName': request.user.username,
    # }

    return redirect('articles:detail', pk)

@login_required
def rec_create(request, c_pk, a_pk):

    if request.method == 'POST':
        comment = Comment.objects.get(pk=c_pk)
        recomment_form = ReCommentForm(request.POST)
        if recomment_form.is_valid():
            recomment = recomment_form.save(commit=False)
            recomment.comment = comment
            recomment.user = request.user
            recomment.save()
        return redirect('articles:detail', a_pk)

@login_required
def rec_detail_create(request, c_pk, a_pk):

    if request.method == 'POST':
        comment = Comment.objects.get(pk=c_pk)
        recomment_form = ReCommentForm(request.POST)
        if recomment_form.is_valid():
            recomment = recomment_form.save(commit=False)
            recomment.comment = comment
            recomment.user = request.user
            recomment.save()
        return redirect('articles:rec_detail', c_pk, a_pk)
    


@login_required
def c_delete(request, c_pk, a_pk):

    comment = Comment.objects.get(pk=c_pk)
    comment.delete()

    return redirect("articles:detail", a_pk)

# ????????? ??????
@login_required
def recomment_delete(request, c_pk, a_pk):

    recomment = ReComment.objects.get(pk=c_pk)
    recomment.delete()

    return redirect("articles:rec_detail", c_pk, a_pk)


@login_required
def rec_delete(request, rec_pk, c_pk, a_pk):

    recomment = ReComment.objects.get(pk=rec_pk)
    recomment.delete()

    return redirect('articles:rec_detail', c_pk, a_pk)


@login_required
def like(request, pk):

    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)

        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            is_liked = False
        else:
            article.like_users.add(request.user)
            is_liked = True

        like_count = article.like_users.count()
        
        context = {
            'is_liked': is_liked,
            'likeCount': like_count,

        }
        return JsonResponse(context)
    return redirect('accounts:login')

@login_required
def c_like(request, c_pk):

    if request.user.is_authenticated:

        comment = Comment.objects.get(pk=c_pk)

        if request.user in comment.like_users.all():
            comment.like_users.remove(request.user)
            comment_is_liked = False
        else:
            comment.like_users.add(request.user)
            comment_is_liked = True

        like_count = comment.like_users.count()

        context = {
            'comment_is_liked': comment_is_liked,
            'like_count': like_count,
        }

        return JsonResponse(context)
    return redirect('accounts:login')


@login_required
def rec_like(request, c_pk, a_pk):

    if request.user.is_authenticated:

        comment = Comment.objects.get(pk=c_pk)

        if request.user in comment.like_users.all():
            comment.like_users.remove(request.user)
        else:
            comment.like_users.add(request.user)

        return redirect('articles:rec_detail', c_pk, a_pk)
    return redirect('accounts:login')

def search(request):
    keyword = request.GET.get("keyword", "")  # ?????????

    if keyword:
        products = Product.objects.filter(
            Q(product_name__icontains=keyword) | Q(brand__icontains=keyword)
        ).distinct()
        articles = Article.objects.filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword)
        ).distinct()
        context = {
            "products": products,
            "articles": articles,
            "keyword": keyword,
        }
        return render(request, "articles/search.html", context)
