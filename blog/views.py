from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import markdown
from .models import Blog

md = markdown.Markdown()

def blog(request):
    articles = Blog.objects.order_by('-updated_at').filter(is_published=True)

    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    context = {
        'articles': paged_articles
    }

    return render(request, 'pages/blog.html', context)

def article(request, blog_id):
    article = get_object_or_404(Blog, pk=blog_id)

    content = md.convert(article.content)

    context = {
        "entry": md.convert(article.content),
        "title": article.title,
        "lead": article.lead,
        "category": article.category,
        "author": article.author,
        "updated_at": article.updated_at,
        "read_number": article.read_number
    }

    return render(request, 'pages/article.html', context)