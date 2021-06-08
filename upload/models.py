from django.db import models


class Upload(models.Model):
    image_file = models.ImageField(max_length=300, unique=True)

    def __str__(self):
        return self.image_file
