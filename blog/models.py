from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField


# class PublisherManager(models.Manager):
#     def get_queryset(self):
#         return super(PublisherManager, self).get_queryset()\
#             .filter(status='publicada')
# Category.post_set.all()
class Category(models.Model):
    name = models.CharField(max_length=255)
    published = models.DateTimeField(default=timezone.now)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    title = models.CharField(max_length=255, verbose_name='Título')
    subtitle = models.CharField(max_length=255, verbose_name='Subtítulo')
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Autor')
    category = models.ManyToManyField(Category, verbose_name='Categoria')
    content = RichTextField(verbose_name='Conteúdo')
    published = models.DateTimeField(default=timezone.now)
    create_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS, default='rascunho')
    image = models.ImageField(
        upload_to='blog', verbose_name='Imagem', blank=True, null=True)

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    # objects = models.Manager()
    # published = PublisherManager()
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_absolute_url_edit(self):
        return reverse('post_edit', args=[self.slug])

    def __str__(self):
        return f"{self.title}"

    def view_image(self):
        return mark_safe('<img src="%s" width="400px"/>' % self.image.url)
    view_image.short_description = 'Visualização da imagem'
    view_image.allow_tags = True


@receiver(post_save, sender=Post)
def inser_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()
