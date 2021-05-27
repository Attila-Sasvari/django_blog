from django.contrib import admin

from .models import Blog, BlogCounts, Tag


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'updated_at')
    list_display_links = ('id', 'title')
    list_filter = ('is_published', 'updated_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'category', 'content', 'lead')
    list_per_page = 5

    prepopulated_fields = {
        "slug": (
            "title",
        )
    }
    date_hierarchy = "created_at"
    save_on_top = True


class BlogCountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_id', 'read_number', 'stars_number')
    list_filter = ('read_number', 'stars_number')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCounts, BlogCountsAdmin)
admin.site.register(Tag, TagAdmin)
