from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']  # Only include content in the form, as the user is automatically assigned.

    # Customize the content field widget
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full md:w-96 p-2 border border-gray-300 rounded-lg',  # Tailwind CSS classes
            'rows': 10,  # You can customize the number of rows here
        })
    )
