from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Custom Manager for Published Posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class post(models.Model):  # Keeping the lowercase 'post' as per your request
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    tittle = models.CharField(max_length=100)  # Keeping the spelling as is
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')  # Keeping the uppercase 'Status'

    # Managers
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager for published posts

    class Meta:
        ordering = ['-publish']  # Corrected to use a list

    def __str__(self):
        return self.tittle  # Keeping the spelling as is

    def get_absolute_url(self):
        return reverse('blog:post_detail', 
                       args=[self.publish.year, 
                             self.publish.strftime('%m'), 
                             self.publish.strftime('%d'), 
                             self.slug])
