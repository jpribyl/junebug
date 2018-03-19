from django import forms
from .models import Chirp

class ChirpModelForm(forms.ModelForm):
    class Meta:
        model = Chirp 
        fields = [
            "user",
            "content"
        ]
        # exclude = ["user"]

    # put the field name after clean for validations
    # see docs for more info
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")

        if content == "abc":
            raise forms.ValidationError("Cannot be abc")

        return content
