from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "description", "photo", "user")
    search_fields = ("title", "user")
# Register your models here.
