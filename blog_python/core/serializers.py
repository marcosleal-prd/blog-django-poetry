import logging

from rest_framework import serializers

from blog_python.core.models import Category
from blog_python.core.models import Post
from blog_python.core.models import Tag

logger = logging.getLogger(__name__)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        ref_name = "Post"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        ref_name = "Tag"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        ref_name = "Category"
