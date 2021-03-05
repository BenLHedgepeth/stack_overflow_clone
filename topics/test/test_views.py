
from django.test import TestCase
from django.urls import reverse

from ..models import Topic

class TestTopicListMainPage(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.topics = Topic.objects.none()
        cls.url = reverse("topics:main")

    def test_topics_main_page_no_topics(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplatedUsed(response, "topics.html")
        self.assertContains(
            response, "Whoops...no topics are being talked about"
        )
