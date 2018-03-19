from django import forms
from .models import Chirp

class ChirpModelForm(forms.ModelForm):

    content = forms.CharField(
        label='', 
        widget=forms.Textarea(
            attrs={'placeholder': "your chirp goes here", 
                   "class": "form-control"}))

    class Meta:
        model = Chirp 
        fields = [
            # "user",
            "content"
        ]
        # exclude = ["user"]

    # validations may be in the form, or the model, or in their own module
    # see docs for more info

    # put the field name after clean for validations
    # def clean_content(self, *args, **kwargs):
        # content = self.cleaned_data.get("content")

        # if content == "abc":
            # raise forms.ValidationError("Cannot be abc")

        # return content
