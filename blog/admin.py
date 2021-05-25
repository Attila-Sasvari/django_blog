from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'updated_at')
  list_display_links = ('id', 'title')
  list_filter = ('is_published', 'updated_at')
  list_editable = ('is_published',)
  search_fields = ('title', 'category', 'content', 'lead')
  list_per_page = 5

admin.site.register(Blog, BlogAdmin)