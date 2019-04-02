from django import forms


class TweetCreateForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, max_length=300)
