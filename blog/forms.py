from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):

    text = forms.CharField(
        widget=forms.TextInput(attrs={"class": "textarea", "size": 64})
    )

    class Meta:
        model = Blog
        fields = ["text"]
