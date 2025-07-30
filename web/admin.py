import markdown
from django.contrib import admin
from .models import Post, Work
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'content_preview')

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'content_preview')
        }),
        ('Дополнительно', {
            'fields': ('created_at',),
        }),
    )

    def short_content(self, obj):
        return obj.content[:60] + '...'
    short_content.short_description = "Описание"

    def content_preview(self, obj):
        if not obj.content:
            return "-"
        html = markdown.markdown(obj.content)
        return format_html('<div style="border:1px solid #ddd;padding:10px;">{}</div>', html)
    content_preview.short_description = "Markdown-превью"


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'created_at', 'image_preview')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'image_preview')

    def short_description(self, obj):
        return obj.description[:60] + '...'
    short_description.short_description = "Описание"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" style="object-fit: contain;" />', obj.image.url)
        return "—"
    image_preview.short_description = "Изображение"
