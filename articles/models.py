import os
from django.db import models


# Create your models here.
def get_filename(file_path):
    base_name = os.path.basename(file_path)
    ext = os.path.splitext(base_name)
    return ext


def image_name(instance, filename):
    ext = get_filename(filename)
    final_name = f'{instance.title}-{instance.id}.{ext}'
    return f'media/{instance.title}/{filename}'


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to=image_name, default="default.png", blank=True)
    # TODO add in author

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + " ..... "
