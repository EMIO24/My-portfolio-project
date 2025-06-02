# portfolio/forms.py

from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    """
    Django form for the ContactMessage model.
    """
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input-field', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input-field', 'placeholder': 'your.email@example.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input-field', 'placeholder': '+1 (XXX) XXX-XXXX'}),
            'subject': forms.TextInput(attrs={'class': 'form-input-field', 'placeholder': 'Project Inquiry, Collaboration, etc.'}),
            'message': forms.Textarea(attrs={'class': 'form-input-field', 'placeholder': 'Your message...', 'rows': 6}),
        }
        # Add help text for fields if needed
        help_texts = {
            'phone_number': 'Optional: Enter your phone number including country code (e.g., +1234567890).',
        }
