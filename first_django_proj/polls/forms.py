from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    # name = forms.CharField(max_length=200)
    # email = forms.EmailField(help_text='Enter your email address')
    # message = forms.CharField(widget=forms.Textarea, label="Your message")
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {'message': 'Your message'}
        help_texts = {'email': 'Your email address is needed.'}

    # def clean(self):
    #     super(ContactForm, self).clean()
    #     email = self.cleaned_data.get('email')
    #     if '.ac.ir' not in email or '.edu' not in email:
    #         raise forms.ValidationError('Please enter your academic email address!')
    #     else:
    #         return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@ac.ir' not in email and '@edu' not in email:
            raise forms.ValidationError('Please enter your academic email address!')
        else:
            return email