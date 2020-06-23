from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from fashion.settings import LOGGING
from django.contrib.auth import forms, authenticate, login
from django.shortcuts import render, redirect
from django import forms
from django.contrib.sites.shortcuts import get_current_site
from .forms import SignUpForm
import logging.config
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

def signup_view(request):
        logger.debug("attempt to signup")
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(request.POST)
                user.refresh_from_db()
                user.is_active = False
                user.save()
                login(request, user)
                current_site = get_current_site(request)
                subject = 'Please Activate Your Account'
                message = render_to_string('registration/confirm_registration.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                request.user.email_user(subject, message)
                return HttpResponseRedirect('sent/')
        else:
            form = SignUpForm()
        return render(request, 'registration/register.html', {'form': form})

def activation_sent_view(request):
    logger.debug("activation sent")
    return render(request, 'registration/confirmation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.account.verification = True
        user.save()
        login(request, user)
        logger.debug("activation")
        return redirect('accounts:login')
    else:
        logger.debug("activation fail")
        return redirect('accounts:register')





