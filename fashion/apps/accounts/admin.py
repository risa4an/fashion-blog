from gevent.pool import Pool

from django.contrib import admin
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from jinja2 import Template
from .tokens import account_activation_token
from .models import Profile
import datetime

# Register your models here.
def send(queryset_user):
    template = Template("""
    Date/time: {{ now() }}
    Hi {{ user.username }} ({{ user.email }}),
    Please click the following link to confirm your registration:
    http://127.0.0.1:8002/activate/{{ uid }}/{{ token }}
    """)

    template.globals['now'] = datetime.datetime.utcnow
    template.globals['user'] = queryset_user.user
    template.globals['uid'] = urlsafe_base64_encode(force_bytes(queryset_user.user.pk))
    template.globals['token'] = account_activation_token.make_token(queryset_user.user)

    subject = 'Please Activate Your Account'
    queryset_user.user.email_user(subject, template.render())

def send_signup_confirmation(modeladmin, request, queryset):
    pool = Pool(5)
    pool.map(send, queryset)

send_signup_confirmation.short_description = "Send signup confirmation"

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'verification']
    ordering = ['user']
    actions = [send_signup_confirmation]


admin.site.register(Profile, ProfileAdmin)