import textwrap

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Topic, Tag
from ..forms import TopicForm

# class TestTopicTextField(TestCase):
#     '''Verify that the markdown entered by a user in a
#     form textfield is saved in the DB as HTML'''
#     pass
#
#     @classmethod
#     def setUpTestData(cls):
#         markdown = textwrap.dedent("""
#             #How To Create A Markdown List
#             * Item 1
#             * Item 2
#             * Item 3
#         """)
#         cls.user = User.objects.create_user("User")
#         a = Tag.objects.create(name="HTML")
#         cls.data = {
#             'heading': "HTML unordered list",
#             'text': markdown,
#             'tags': [a]
#         }
#         cls.form = TopicForm(cls.data)
#         cls.form.is_valid()
#         cls.topic = cls.form.save(commit=False)
#         cls.topic.author = cls.user
#         cls.topic.save()
#         cls.form.save_m2m()
#
#     def test_markdown_to_html_pass(self):
#         self.assertHTMLEqual(self.topic.text, """
#             <h1>How To Create A Markdown List</h1>
#             <ul>
#                 <li>Item 1</li>
#                 <li>Item 2</li>
#                 <li>Item 3</li>
#             </ul>
#         """
#         )

class TestTopicEditTextField(TestCase):
    '''Verify that markdown saved in an existing Topic is considered
    as initial data when the Topic is selected to be edited'''

    @classmethod
    def setUpTestData(cls):

        cls.markdown = textwrap.dedent("""
            #How To Create A Markdown List
            * Item 1
            * Item 2
            * Item 3
        """)

        user = User.objects.create_user("User")
        a = Tag.objects.create(name="HTML")
        data = {
            'heading': "HTML unordered list",
            'text': cls.markdown,
            'author': user
        }
        topic = Topic.objects.create(**data)
        topic.tags.add(a)
        cls.form = TopicForm(initial={
            'heading': topic.heading,
            'text': topic.text
        })

    def test_topic_form_initial_edit_values(self):
        self.assertEqual(self.form['heading'].value(), "HTML unordered list")
        self.assertEqual(
            self.form['text'].value(),
            self.markdown
        )
