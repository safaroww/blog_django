from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics')
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.name