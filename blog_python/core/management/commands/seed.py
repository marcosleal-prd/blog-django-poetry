from typing import List

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from blog_python.core.management.commands.seedsuperuser import create_user
from blog_python.core.models import Category
from blog_python.core.models import Post
from blog_python.core.models import PostTag
from blog_python.core.models import Tag
from blog_python.core.models import UserRole


def create_category(name: str, description: str) -> Category:
    return Category.objects.create(name=name, description=description)


def create_user_role(user: User, role: str) -> UserRole:
    return UserRole.objects.create(user=user, role=role)


def create_tag(name: str) -> Tag:
    return Tag.objects.create(name=name)


def create_post(
    title: str,
    desc: str,
    content: str,
    author: User,
    category: Category,
    keywords: str,
    tags: List[Tag],
) -> Post:
    with transaction.atomic():
        post = Post.objects.create(
            title=title,
            description=desc,
            content=content,
            author=author,
            category=category,
            keywords=keywords,
        )

        for tag in tags:
            PostTag.objects.create(post=post, tag=tag)

    return post


def seed():
    # Users
    admin = User.objects.get(username="admin")
    publisher = create_user("publisher", "test")
    author = create_user("author", "test")

    # Roles
    create_user_role(user=admin, role="Admin")
    create_user_role(user=publisher, role="Publisher")
    create_user_role(user=author, role="Author")

    # Tags
    tag_1 = create_tag(name="Python")
    tag_2 = create_tag(name="Django")
    tag_3 = create_tag(name="Docker")
    tag_4 = create_tag(name="Kubernetes")
    tag_5 = create_tag(name="Poetry")

    # Categories
    category_1 = create_category(
        name="Web Development",
        description="Blog de desenvolvimento web sobre HTML5, CSS3, Web...",
    )
    category_2 = create_category(
        name="Programming",
        description="Blog de programação sobre PHP, JavaScript, jQuery...",
    )
    category_3 = create_category(
        name="Blog",
        description="Artigos e vídeo aulas sobre desenvolvimento...",
    )

    # Posts
    create_post(
        title="Os 5 melhores frameworks de Python",
        desc="Ferramentas para facilitar o desenvolvimento do projeto.",
        content="O Python é uma das linguagens de programação de alto nível.",
        author=admin,
        category=category_1,
        tags=[tag_1, tag_2, tag_3],
        keywords="Python,Frameworks,TOP 5",
    )
    create_post(
        title="Why we deploy machine learning models with Go — not Python",
        desc="There’s more to production machine learning than Python scripts",
        content="There’s more to production machine learning than Python.",
        author=publisher,
        category=category_2,
        tags=[tag_1, tag_3, tag_5],
        keywords="Python,Machine Learning,Models,GO",
    )
    create_post(
        title="Top 10 Magic Commands in Python to Boost your Productivity",
        desc="Implementation of important IPython magic commands",
        content="Python is not only the most versatile programming language.",
        author=author,
        category=category_3,
        tags=[tag_4, tag_3, tag_5],
        keywords="Python,Magic Commands,Productivity,IPython",
    )


class Command(BaseCommand):
    help = "Create data"

    def handle(self, *args, **options):
        seed()
