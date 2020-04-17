import uuid

from django.contrib.auth.models import User
from django.contrib.postgres.indexes import BrinIndex
from django.db import models

STATUS_CHOICE = (
    ("Drafted", "Drafted"),
    ("Published", "Published"),
    ("Rejected", "Rejected"),
    ("Trashed", "Trashed"),
)

ROLE_CHOICE = (
    ("Admin", "Admin"),
    ("Publisher", "Publisher"),
    ("Author", "Author"),
)


class StandardModelMixin(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created at"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True
        indexes = [BrinIndex(fields=["created_at"])]


class UserRole(StandardModelMixin):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="User"
    )
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICE, verbose_name="Role"
    )

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ["-id"]


class Category(StandardModelMixin):
    name = models.CharField(max_length=30, unique=True, verbose_name="Name")
    description = models.CharField(max_length=255, verbose_name="Description")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(StandardModelMixin):
    name = models.CharField(max_length=30, unique=True, verbose_name="Name")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Post(StandardModelMixin):
    title = models.CharField(max_length=100, unique=True, verbose_name="Title")
    description = models.CharField(max_length=255, verbose_name="Description")
    content = models.TextField(verbose_name="HTML Content")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Author"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Category"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICE,
        default="Drafted",
        verbose_name="Status",
    )
    keywords = models.TextField(
        max_length=500, blank=True, verbose_name="Keywords"
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title


class PostTag(StandardModelMixin):
    post = models.ForeignKey(
        Post,
        related_name="posts",
        on_delete=models.CASCADE,
        verbose_name="Post",
    )
    tag = models.ForeignKey(
        Tag, related_name="tags", on_delete=models.CASCADE, verbose_name="Tag",
    )

    class Meta:
        verbose_name = "Post Tag"
        verbose_name_plural = "Post Tags"
        constraints = [
            models.UniqueConstraint(
                fields=["post", "tag"], name="unique_tag_per_post"
            )
        ]
