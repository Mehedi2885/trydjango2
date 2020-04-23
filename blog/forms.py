from django import forms
from .models import Article


class ArticleModelForms(forms.ModelForm):
    title = forms.CharField(label='Article title',
                            widget=forms.TextInput(attrs={"placeholder": "My Article Title"}))
    content = forms.CharField(required=False, widget=forms.Textarea)
    active = forms.BooleanField(required=False)

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]
