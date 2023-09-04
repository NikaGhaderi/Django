from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    # how you override what comes in by default
    title = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'fill me up bitch'}))
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "new_class_name",
        "id": "my-id-for-textarea",
        "rows": 5,
        "cols": 50
    }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "nik" not in title:
            raise forms.ValidationError("This is not a valid title.")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith('edu'):
            raise forms.ValidationError("This is not a valid email.")
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'fill me up bitch'}))
    # now that we changed the widget to textarea, this field is not required anymore by default.
    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "new_class_name",
        "id": "my-id-for-textarea",
        "rows": 5,
        "cols": 50
    }))
    price = forms.DecimalField(initial=199.99)