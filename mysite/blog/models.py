import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model): 
    objects = models.Manager
    published = PublishedManager() # invoking our custom manager
    id = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250) 
    slug =models.SlugField(max_length=250, unique_for_date='publish') 
    body = models.TextField() 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Status(models.TextChoices): 
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)
    
    class Meta: 
        ordering = ['-publish'] 
        indexes = [ models.Index(fields=['-publish']), ]
        # db_table = 'Post'  # to specify table name

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self): 
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    
    