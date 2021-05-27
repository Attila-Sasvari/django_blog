from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min, Q, Count, Sum, F
from blog.models import Blog, BlogCounts
from django.contrib.auth.models import User
from django.db.models.functions import TruncDate
from datetime import datetime
from django.contrib import messages
from .models import DailyStats
from django.http import JsonResponse


def dashboard(request):

    articles_count = Blog.objects.count()

    oldest_article = Blog.objects.aggregate(Min('created_at'))

    authors_count = Blog.objects.aggregate(Count('author', distinct=True))

    read_number_stats = BlogCounts.objects.aggregate(
        Avg('read_number'), Max('read_number'), Min('read_number'), Sum('read_number'))

    articles_by_day = Blog.objects\
        .annotate(created_day=TruncDate('created_at'))\
        .values('created_day')\
        .annotate(article_count=Count('created_day'))\
        .order_by()

    highest_read = Blog.objects.order_by('-blogcounts__read_number')[:3]

    context = {
        "articles_count": articles_count,
        "articles_by_day": articles_by_day,
        "authors_count": authors_count,
        "oldest_article": oldest_article,
        "read_number_stats": read_number_stats,
        "highest_read": highest_read
    }

    return render(request, 'dashboard.html', context)


def update_daily(request):
    if request.method == 'POST':

        articles_count = Blog.objects.count()
        authors_count = Blog.objects.aggregate(Count('author', distinct=True))

        read_number_stats = BlogCounts.objects.aggregate(
            Avg('read_number'), Max('read_number'), Min('read_number'), Sum('read_number'))

        print(read_number_stats)

        """ highest_read_title = Blog.objects.order_by(
            '-blogcounts__read_number')[:1]["title"] """
        highest_read_title = "valamilyen"

        daily_stats_obj = DailyStats(articles_count=articles_count, authors_count=authors_count["author__count"],
                                     highest_read_title=highest_read_title, read_number_avg=read_number_stats["read_number__avg"],
                                     read_number_max=read_number_stats["read_number__max"],
                                     read_number_min=read_number_stats["read_number__min"], read_number_sum=read_number_stats["read_number__sum"])

        daily_stats_obj.save()

        return JsonResponse({'message': 'Daily Stats have been saved to database.'})
