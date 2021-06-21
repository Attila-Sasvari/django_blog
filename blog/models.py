from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.shortcuts import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    lead = models.TextField(blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    cover_img = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, default=settings.DEFUALT_COVER_IMG)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    content = models.TextField(default="-")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ["-updated_at"]
        app_label = "blog"

    @property
    def img_url(self):
        return self.cover_img.url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        post = Blog.objects.get(pk=self.id)
        obj, created = BlogCounts.objects.get_or_create(blog_id=post)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})


class BlogCounts(models.Model):
    blog_id = models.OneToOneField(Blog, on_delete=models.CASCADE)
    read_number = models.PositiveIntegerField(default=0)
    stars_number = models.PositiveIntegerField(default=0)
