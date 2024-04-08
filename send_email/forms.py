from django import forms
class ContactForm(forms.Form):
    subject = forms.CharField(label='Betreff', max_length=100, required=True)
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='E-Mail', max_length=254, required=True)
    message = forms.CharField(label='Nachricht', widget=forms.Textarea, required=True)
