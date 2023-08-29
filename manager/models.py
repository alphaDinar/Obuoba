from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Program(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    host = models.CharField(max_length=300)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    image = CloudinaryField("Image" ,folder='Obuoba', resource_type='auto')
    slug = models.SlugField(max_length=500, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name} + {self.description[:2]}')
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=5000)
    CATEGORY = (
        ('news', 'news'),
        ('politics', 'politics'),
        ('business', 'business'),
        ('entertainment', 'entertainment'),
        ('sports', 'sports'),
        ('technology', 'technology'),
        ('opinion', 'opinion'),
        ('lifestyle', 'lifestyle'),
        ('gallery', 'gallery'),
        ('obituary', 'obituary')
    )
    category = models.CharField(max_length=100, choices=CATEGORY, default='news')
    image = CloudinaryField("Image" ,folder='Obuoba', resource_type='auto')
    video = CloudinaryField("Video" ,folder='Obuoba', resource_type='auto')
    TYPE = (
        ('image', 'image'),
        ('video', 'video'),
    )
    type = models.CharField(max_length=50, choices=TYPE, default='image')
    tags = models.CharField(max_length=300)
    source = models.CharField(max_length=300)
    impressions = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, blank=True)
    def save( self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title[:50])
        super().save(*args,**kwargs)
    def __str__(self):
        return self.title
