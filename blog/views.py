from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import markdown
from .models import Blog, BlogCounts
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required

md = markdown.Markdown()


def blog(request):
    articles = Blog.objects.order_by('-updated_at').filter(is_published=True)
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    context = {
        'articles': paged_articles,
        'to_edit': False
    }

    return render(request, 'blog/blog.html', context)

def about(request):
    return render(request, 'about.html')


@login_required
def my_articles(request):
    articles = Blog.objects.order_by(
        '-updated_at').filter(is_published=True).filter(author=request.user)
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    context = {
        'articles': paged_articles,
        'to_edit': True
    }

    return render(request, 'blog/blog.html', context)


@login_required
def my_drafts(request):
    articles = Blog.objects.order_by(
        '-updated_at').filter(is_published=False).filter(author=request.user)
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    context = {
        'articles': paged_articles,
        'to_edit': True
    }

    return render(request, 'blog/blog.html', context)


def article(request, slug):
    article = get_object_or_404(Blog, slug=slug)
    article.blogcounts.read_number += 1
    article.blogcounts.save(update_fields=['read_number'])

    context = {
        "id": article.id,
        "slug": article.slug,
        "entry": md.convert(article.content),
        "title": article.title,
        "lead": article.lead,
        "tags": article.tags,
        "category": article.category,
        "author": article.author,
        "updated_at": article.updated_at,
        "read_number": article.blogcounts.read_number,
        "stars_number": article.blogcounts.stars_number,
        "cover_img": article.cover_img.url
    }

    return render(request, 'blog/article.html', context)


@transaction.atomic
@login_required
def add_star(request, slug):
    if request.method == 'POST':
        article = get_object_or_404(Blog, slug=slug)
        article.blogcounts.stars_number += 1
        article.blogcounts.save(update_fields=['stars_number'])

        context = {
            "id": article.id,
            "slug": article.slug,
            "entry": md.convert(article.content),
            "title": article.title,
            "lead": article.lead,
            "category": article.category,
            "author": article.author,
            "updated_at": article.updated_at,
            "read_number": article.blogcounts.read_number,
            "stars_number": article.blogcounts.stars_number,
            "cover_img": article.cover_img,
        }

        return render(request, 'blog/article.html', context)
    else:
        return


def search_blog(request):
    articles = Blog.objects.order_by('-updated_at')
    #articles_list = []

    category_list = {
        "tech": 'tech',
        "fitnes": 'fitnes',
        "money": 'money'
    }

    if 'content' in request.GET:
        content = request.GET['content']
        if content:
            articles_list = articles.filter(content__icontains=content)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            articles_list = articles.filter(category__iexact=category)

    if 'lead' in request.GET:
        lead = request.GET['lead']
        if lead:
            articles_list = articles.filter(lead__icontains=lead)

    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            articles_list = articles.filter(title__icontains=title)

    paginator = Paginator(articles_list, 2)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    context = {
        'articles': paged_articles,
        'category_list': category_list,
        'to_edit': False
    }

    return render(request, 'blog/blog.html', context)

@login_required
def edit_article(request, blog_id=1):
    return HttpResponseRedirect(reverse("admin:blog_blog_change", args=(blog_id,)))
