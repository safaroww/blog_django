from django.db import models
from django.urls import reverse

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author", kwargs={"pk": self.pk})
    