from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import markdown
from .models import Blog
from django.db import transaction
from django.contrib import messages

md = markdown.Markdown()

def blog(request):
    articles = Blog.objects.order_by('-updated_at').filter(is_published=True)

    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    context = {
        'articles': paged_articles
    }

    return render(request, 'blog/blog.html', context)

def article(request, blog_id):
    article = get_object_or_404(Blog, pk=blog_id)

    context = {
        "id": article.id,
        "entry": md.convert(article.content),
        "title": article.title,
        "lead": article.lead,
        "category": article.category,
        "author": article.author,
        "updated_at": article.updated_at,
        "read_number": article.read_number,
        "stars_number": article.stars_number
    }

    article.read_number += 1
    article.save()

    return render(request, 'blog/article.html', context)

@transaction.atomic
def add_star(request, blog_id):
    if request.method == 'POST':
        article = get_object_or_404(Blog, pk=blog_id)
        article.stars_number += 1
        article.save(update_fields=['stars_number'])
        messages.success(request, 'Star added!')

        context = {
            "id": article.id,
            "entry": md.convert(article.content),
            "title": article.title,
            "lead": article.lead,
            "category": article.category,
            "author": article.author,
            "updated_at": article.updated_at,
            "read_number": article.read_number,
            "stars_number": article.stars_number
        }
        return render(request, 'blog/article.html', context)
    else:
        return