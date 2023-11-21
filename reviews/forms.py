from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(required=True, max_length=55, min_length=5)
