from django.contrib import admin
from blog.models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'published')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    date_hierarchy = 'published'
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published', 'status')
    list_display_links = ('id', 'title')
    list_filter = ('author', 'status')
    raw_id_fields = ('author',)
    date_hierarchy = 'published'
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    ordering = ('-published',)
