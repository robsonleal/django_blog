from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    slug = models.SlugField(max_length=255)
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

    def __str__(self):
        return f"{self.title}"
