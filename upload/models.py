from django.db import models
from PIL import Image


class Upload(models.Model):
    image_file = models.ImageField(max_length=300, unique=True)

    def __str__(self):
        return self.image_file
    
    def save(self):
        super().save()

        img = Image.open(self.image_file.path)

        width, height = img.size

        if height > 400 or width > 400:
            ratio = width / height
            new_height = 300
            new_width = int(ratio * new_height)
            img.resize((new_width, new_height))
            img.save(self.image.path)
