from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + self.author

    def get_absolute_url(self):
        return reverse('home')
