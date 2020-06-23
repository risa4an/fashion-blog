
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from jinja2 import Template
from .tokens import account_activation_token
from .models import Account
import datetime
from multiprocessing import Process, Queue, Pool

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
    # return subject, template.render()
    queryset_user.user.email_user(subject, template.render())


q = Queue()

def putUserInQ(queryset):
    for quser in queryset:
        q.put(quser)

def sendQuser():
    while not q.empty():
        send(q.get())


def send_signup_confirmation(modeladmin, request, queryset):
    process_one = Process(target = putUserInQ, args = (queryset, ))
    process_two = Process(target = sendQuser, args = (None, ))

    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()



send_signup_confirmation.short_description = "Send signup confirmation"

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'verification']
    ordering = ['user']
    actions = [send_signup_confirmation]


admin.site.register(Account, AccountAdmin)