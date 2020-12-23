from django import forms

from .models import *


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        # widgets attribute is an HTML form element with columns = 80 allows to user enough room to write entries.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

