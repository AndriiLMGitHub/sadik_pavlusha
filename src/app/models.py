import random
from django.db import models


class GalleryPhoto(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return f'Image gallery {random.randint(0, 10000)}'
