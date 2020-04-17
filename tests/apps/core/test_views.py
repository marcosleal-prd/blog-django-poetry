from django.test import Client
from django.test import TestCase


class PostV1RouteTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.basename = "posts_v1"

    def test_get_all_should_return_data(self):
        pass
