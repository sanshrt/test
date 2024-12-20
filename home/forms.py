from django import forms
from django.contrib.auth.models import User
from .models import Register

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), initial="")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password", initial="")
    age = forms.IntegerField(required=False, min_value=0, label="Age", initial=None)  # Make age optional with no default

    class Meta:
        model = Register
        fields = ['name', 'email_id','college_name', 'phone_number', 'department', 'age']
        widgets = {
            'name': forms.TextInput(attrs={'value': ''}),
            'email_id': forms.EmailInput(attrs={'value': ''}),
            'phone_number': forms.TextInput(attrs={'value': ''}),
            'college_name':forms.TextInput(attrs={'value':''}),
            'department': forms.TextInput(attrs={'value': ''}),
            'age': forms.NumberInput(attrs={'value': ''}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['email_id'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email_id']
        )
        register = super().save(commit=False)
        register.user = user
        if commit:
            register.save()
        return register
