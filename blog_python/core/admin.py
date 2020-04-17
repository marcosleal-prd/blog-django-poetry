from django.contrib import admin

from blog_python.core.models import Category
from blog_python.core.models import Post
from blog_python.core.models import PostTag
from blog_python.core.models import Tag
from blog_python.core.models import UserRole


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "created_at", "updated_at")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "author",
        "content",
        "category",
        "status",
        "keywords",
        "created_at",
        "updated_at",
    )


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "tag",
        "created_at",
        "updated_at",
    )
