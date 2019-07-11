from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    sender = forms.EmailField()
    number = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    author = forms.CharField(max_length = 50)
    body= forms.CharField(widget= forms.Textarea)
