from django.db import models
from PIL import Image


class Upload(models.Model):
    image_file = models.ImageField(max_length=300, unique=True)

    def __str__(self):
        return self.image_file
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print("Saving into media folder.")
        
        img = Image.open(self.image_file.path)
        width, height = img.size

        if height > 500 or width > 500:
            ratio = width / height
            new_height = 300
            new_width = int(ratio * new_height)
            img.thumbnail((new_width, new_height), Image.ANTIALIAS)
            img.save(self.image.path, format='JPEG', quality=60)

