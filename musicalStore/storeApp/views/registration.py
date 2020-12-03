from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from storeApp.Controllers.DBController import DBController


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
        db.CreateUser(request.POST)
        return HttpResponseRedirect(reverse('confirm_email'))


def confirm_email(request):
    return HttpResponse(render(request, 'storeApp/email_confirm_page.html'))

