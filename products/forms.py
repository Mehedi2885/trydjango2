from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Product title',
                            widget=forms.TextInput(attrs={"placeholder": "My Title"}))
    description = forms.CharField(required=False, widget=forms.Textarea)
    price = forms.DecimalField(initial=100)
    summery = forms.CharField(required=False)

    class Meta:

        model = Products
        fields = [
            'title',
            'description',
            'price',
            'summery'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='Product title',
                            widget=forms.TextInput(attrs={"placeholder": "My Title"}))
    description = forms.CharField(required=False, widget=forms.Textarea)
    price = forms.DecimalField(initial=100)
    summery = forms.CharField(required=False)
