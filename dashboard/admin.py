from django.contrib import admin

from .models import DailyStats


class DailyStatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'articles_count', 'read_number_sum', 'timestamp', 'authors_count')
    list_filter = ('articles_count', 'read_number_sum', 'timestamp')


admin.site.register(DailyStats, DailyStatsAdmin)
