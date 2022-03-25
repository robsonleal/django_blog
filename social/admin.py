from django.contrib import admin
from social.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'update_at', 'create_at')
    list_display_links = ('id', 'key')
    search_fields = ('key',)
    ordering = ('key',)
    readonly_fields = ('update_at', 'create_at')
