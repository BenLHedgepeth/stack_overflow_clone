
from django import forms

from .models import Topic, Tag

class TopicForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(Tag.objects.all())

    class Meta:
        model = Topic
        fields = ["heading", "text", "tags"]
