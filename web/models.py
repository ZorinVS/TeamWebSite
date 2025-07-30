import markdown
from django.utils.safestring import mark_safe
from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_content_as_html(self):
        return mark_safe(markdown.markdown(self.content))

    class Meta:
        verbose_name = "Статьи | Кейсы"
        verbose_name_plural = "Статьи | Кейсы"

class Work(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='works/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Решения"
        verbose_name_plural = "Решении"
