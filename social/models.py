from django.db import models


class Link(models.Model):
    key = models.CharField(
        verbose_name='Rede Social', max_length=255, unique=True)
    description = models.CharField(verbose_name='Descrição', max_length=255)
    url = models.CharField(max_length=255, null=False, blank=False)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['key']

    def __str__(self):
        return self.key
