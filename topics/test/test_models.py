
from django.db import models
from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Answer, Comment, Tag

class TestTag(TestCase):
    '''Verify that the string representation of a tag is rendered'''

    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag(name="Django")

    def test_tag_str_name(self):
        self.assertEqual(str(self.tag), "Django")


class TestTopic(TestCase):
    pass
