from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(
        required=True,
        label='Nome de usuário',
        help_text='Este valor pode conter apenas letras, números e os\
            seguintes caracteres @/./+/-/_')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail já cadastrado!')
        return email
