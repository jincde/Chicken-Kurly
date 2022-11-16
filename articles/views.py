from django.shortcuts import render, redirect
from .forms import ArticleForm, ReCommentForm
from .models import Article, Comment, ReComment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required  
from django.http import JsonResponse
from products.models import Product
from django.db.models import Q
# Create your views here.


def index(request):

    articles = Article.objects.order_by('-pk')
    comments = Comment.objects.order_by('-pk')

    page = request.GET.get('page', '1')
    paginator = Paginator(articles, 12)
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
    recomments = ReComment.objects.all()

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
        }
        return render(request, "articles/update.html", context)
    return redirect("articles:index")


@login_required
def c_create(request,pk):

    comment = request.POST.get("comment")
    article = Article.objects.get(pk=pk)

    Comment.objects.create(content=comment, article=article, user=request.user)
    
    # 댓글 비동기를 위한 코드
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
def c_delete(request, c_pk, a_pk):

    comment = Comment.objects.get(pk=c_pk)
    comment.delete()

    return redirect("articles:detail", a_pk)

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
def c_like(request, c_pk, a_pk):

    if request.user.is_authenticated:

        comment = Comment.objects.get(pk=c_pk)

        if request.user in comment.like_users.all():
            comment.like_users.remove(request.user)
        else:
            comment.like_users.add(request.user)

        return redirect('articles:detail', a_pk)
    return redirect('accounts:login')

def search(request):
    keyword = request.GET.get("keyword", "")  # 검색어

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
        }
        return render(request, "articles/search.html", context)