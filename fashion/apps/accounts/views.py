from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission, User
class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)




