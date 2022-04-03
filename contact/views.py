from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage


def contact(request):
    send = False
    alert = {}

    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('menssage', '')
        email = EmailMessage(
            'Mensagem do blog Django',
            'De: {} <{}>\nEscreveu:\n\n{}'.format(name, email, message),
            'no-reply@inbox.mailtrap.io',
            ['rrobson9@gmail.com'],
            reply_to=[email]
        )

        try:
            email.send()
            alert = {
                'tag': 'success',
                'message': 'Mensagem enviada com sucesso!'
                }
            send = True

        except:
            send = False
            alert = {
                'tag': 'danger',
                'message': 'Erro ao enviar mensagem!'
            }

    context = {
        'form': form,
        'alert': alert,
        'success': send
    }

    return render(request, 'contact/contact.html', context)
