from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    body = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk, "slug": self.slug})
    



class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post-images/')