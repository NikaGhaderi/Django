from django import forms
from .models import Article


class modelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]