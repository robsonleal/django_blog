from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage


def contact(request):
    send = False

    form = ContactForm(request.POST or None)
    if form.is_valid():
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')
        mensagem = request.POST.get('mensagem', '')
        email = EmailMessage(
            'Mensagem do blog Django',
            'De: {} <{}>\nEscreveu:\n\n{}'.format(nome, email, mensagem),
        )

        try:
            email.send()
            send = True

        except:
            send = False

    context = {
        'form': form,
        'success': send
    }

    return render(request, 'contact/contact.html', context)
