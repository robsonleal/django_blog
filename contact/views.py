from django.shortcuts import render
# from .forms import ContactForm


def contact(request):
    # send = False
    # form = ContactForm(request.POST or None)
    # if form.is_valid():
    #     send = True

    context = {
        'form': '',
        'success': False
    }

    return render(request, 'contact/contact.html', context)
