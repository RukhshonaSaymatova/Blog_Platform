from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "post", "text")
    search_fields = ("title", "user")
# Register your models here.
