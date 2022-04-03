from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome ...'
        }),
        label='Nome',
        required=True
    )

    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu e-mail ...'
        }),
        label='E-mail',
        required=True
    )

    menssage = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={
            'placeholder': 'Digite sua mensagem ...'
        }),
        label='Mensagem',
        required=True
    )
