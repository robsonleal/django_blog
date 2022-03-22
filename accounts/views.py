from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import UserCreationFormWithEmail


class SignUpView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'
