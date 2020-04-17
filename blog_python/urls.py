from django.contrib import admin
from django.urls import include
from django.urls import path

from rest_framework import routers

from blog_python.core import views

router = routers.DefaultRouter()
router.register("categories", views.CategoryViewSet, basename="categories_v1")
router.register("posts", views.ProductViewSet, basename="posts_v1")
router.register("tags", views.TagViewSet, basename="tags_v1")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
]
