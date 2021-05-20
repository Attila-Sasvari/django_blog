from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    CATEGORIES = [
        ("tech", 'tech'),
        ("fitnes", 'fitnes'),
        ("money", 'money'),
    ]
    title = models.CharField(max_length=200)
    lead = models.TextField(blank=False)
    category = models.CharField(
        max_length = 10,
        choices = CATEGORIES,
        default = "tech",
    )
    cover_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(default="-")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    read_number = models.PositiveIntegerField(default=0)
    stars_number = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["updated_at"]

    def save(self, *args, **kwargs):
        #do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        #do_something_else()