from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    query = forms.CharField(widget=forms.Textarea(), help_text='Enter your message here')

    def clean(self):
        data = super(ContactForm, self).clean()
        print(data)

        name = data.get('name')
        email = data.get('email')
        query = data.get('query')
        if len(query) < 100:
            raise forms.ValidationError('MESSAGE SHOULD HAVE MINIMUM 100 CHARACTER')