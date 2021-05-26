from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min, Q, Count, Sum, F
from blog.models import Blog, BlogCounts
from django.contrib.auth.models import User
from django.db.models.functions import TruncDate
from datetime import datetime


def dashboard(request):

    articles_count = Blog.objects.count()

    oldest_article = Blog.objects.aggregate(Min('created_at'))

    authors_count = Blog.objects.aggregate(Count('author', distinct=True))

    read_number_stats = BlogCounts.objects.aggregate(Avg('read_number'), Max('read_number'), Min('read_number'), Sum('read_number'))

    articles_by_day = Blog.objects\
    .annotate(created_day=TruncDate('created_at'))\
    .values('created_day')\
    .annotate(article_count=Count('created_day'))\
    .order_by()

    highest_read = Blog.objects.order_by('-blogcounts__read_number')[:3]
    print(highest_read)




    context = {
        "articles_count": articles_count,
        "articles_by_day": articles_by_day,
        "authors_count": authors_count,
        "oldest_article": oldest_article,
        "read_number_stats": read_number_stats,
        "highest_read": highest_read
    }

    return render(request, 'dashboard.html', context)

"""     nonzero_stars = Blog.objects.annotate(stars_number=Count('blogcounts.stars_number')).filter(stars_number__gt=1)

    nonzero_stars = Blog.objects.annotate(stars_number=Count('blogcounts.stars_number')).filter(stars_number__gt=1)

    read_number_stats = Blog.objects.aggregate(Avg('blogcounts.read_number'), Max('blogcounts.read_number'), Min('blogcounts.read_number')) """

    

    
"""         "nonzero_stars": nonzero_stars,
        "read_number_stats": read_number_stats, """