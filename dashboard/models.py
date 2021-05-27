from django.db import models
from datetime import datetime


class DailyStats(models.Model):
    articles_count = models.PositiveIntegerField(default=0)
    authors_count = models.PositiveIntegerField(default=0)
    read_number_avg = models.PositiveIntegerField(default=0)
    read_number_max = models.PositiveIntegerField(default=0)
    read_number_min = models.PositiveIntegerField(default=0)
    read_number_sum = models.PositiveIntegerField(default=0)
    highest_read_title = models.TextField(default="-")
    timestamp = models.DateTimeField(auto_now=True, blank=True)
