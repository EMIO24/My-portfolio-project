from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Your name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your email address'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Your phone number (optional)'})
        self.fields['subject'].widget.attrs.update({'placeholder': 'Subject (optional)'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Your message here...'})