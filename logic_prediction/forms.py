from django import forms
choice_fields = [
    (1, "Yes"),
    (0, "No")
    ]
class ChoiceForm(forms.Form):
    choice = forms.ChoiceField(choices=choice_fields, widget=forms.RadioSelect)
