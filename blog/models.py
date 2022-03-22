from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


# class PublisherManager(models.Manager):
#     def get_queryset(self):
#         return super(PublisherManager, self).get_queryset()\
#             .filter(status='publicada')


class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateField(default=timezone.now)
    create_at = models.DateField(auto_now_add=True)
    changed_at = models.DateField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS, default='rascunho'
        )

    # objects = models.Manager()
    # published = PublisherManager()
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_absolute_url_edit(self):
        return reverse('post_edit', args=[self.slug])

    def __str__(self):
        return f"{self.title}"


@receiver(post_save, sender=Post)
def inser_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()
