from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Blog(models.Model):
    CATEGORIES = [
        ("tech", 'tech'),
        ("fitnes", 'fitnes'),
        ("money", 'money'),
    ]
    title = models.CharField(max_length=200)
    lead = models.TextField(blank=False)
    category = models.CharField(
        max_length=10,
        choices=CATEGORIES,
        default="tech",
    )
    cover_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(default="-")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["updated_at"]
        app_label = "blog"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        post = Blog.objects.get(pk=self.id)
        obj, created = BlogCounts.objects.get_or_create(blog_id=post)

    def __str__(self):
        return self.title


class BlogCounts(models.Model):
    blog_id = models.OneToOneField(Blog, on_delete=models.CASCADE)
    read_number = models.PositiveIntegerField(default=0)
    stars_number = models.PositiveIntegerField(default=0)
