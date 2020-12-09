from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django_email_verification import sendConfirm
from storeApp.Controllers.DBController import DBController
from django.core.mail import send_mail
import pdb

db = DBController()


def registration(request):

    return HttpResponse(render(request, 'storeApp/registration.html', {'keys': DBController.UserKeys}))


def registration_submit(request):

    class ErrorMessages:
        PASSWORDS_MISMATCH = 'Passwords do not match.'

    db = DBController()
    keys = db.UserKeys()
    try:
        if request.POST[keys.PASSWORD] != request.POST[keys.CONF_PASSWORD]:
            error_message = ErrorMessages.PASSWORDS_MISMATCH
            raise Exception(error_message)

    except Exception as message:
        return render(request, 'storeApp/registration.html', {
            'error_message': message,
        })
    else:
        user = db.CreateUser(request.POST)
        sendConfirm(user)
        return HttpResponseRedirect(reverse('login'))


def confirm_email(request, user_id):

    user = db.GetUser(user_id)
    # pdb.set_trace()
    # send message
    send_mail('MusicalStore. Sign up confirm', 'Hello from MusicalStore! To confirm your email follow link bellow', 'yarakhovich.kseniya@gmail.com', [user.email])
    message = "Confirmation email was sent to {}.".format(user.email)
    return render(request, 'storeApp/email_confirm.html', {
        'message': message,
    })

