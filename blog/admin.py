from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'updated_at')
  list_display_links = ('id', 'title')
  search_fields = ('title', 'category')
  list_per_page = 5

admin.site.register(Blog, BlogAdmin)