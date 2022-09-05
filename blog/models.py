from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200)
    content = models.TextField(max_length=250)
    # image = models.ImageField(upload_to)
    publish_date = models.DateTimeField(auto_now_add=True)
    # last_updated = models.DateTimeField(auto_now=True)
    # status = models.CharField(max_length=70)
    
    def __str__(self):
        return f"{self.title}"




