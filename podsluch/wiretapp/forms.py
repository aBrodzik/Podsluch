from django import forms


class EditForm(forms.Form):
    start = forms.CharField(max_length=100)
    end = forms.CharField(max_length=100)

