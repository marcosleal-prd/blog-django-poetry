import logging

from rest_framework import viewsets

from blog_python.core.models import Category
from blog_python.core.models import Post
from blog_python.core.models import Tag
from blog_python.core.serializers import CategorySerializer
from blog_python.core.serializers import PostSerializer
from blog_python.core.serializers import TagSerializer

logger = logging.getLogger(__name__)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by("-created_at").all()
    serializer_class = PostSerializer
    filterset_fields = "__all__"


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.order_by("-created_at").all()
    serializer_class = TagSerializer
    filterset_fields = "__all__"


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.order_by("-created_at").all()
    serializer_class = CategorySerializer
    filterset_fields = "__all__"
