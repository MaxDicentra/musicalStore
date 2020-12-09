from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from storeApp.Controllers.DBController import DBController

db = DBController()


def edit_profile(request):
    user_info, address = db.GetUserData(request.user.id, request.user)
    if request.POST.get('confirm', False):
        db.EditUser(request.POST, request.user.id)
        user_info, address = db.GetUserData(request.user.id, request.user)
        return HttpResponse(render(request, 'storeApp/edit_profile.html', {'keys': DBController.UserKeys,
                                                                           'user': request.user,
                                                                           'user_info': user_info,
                                                                           'address': address, }))

    return HttpResponse(render(request, 'storeApp/edit_profile.html', {'keys': DBController.UserKeys,
                                                                       'user': request.user,
                                                                       'user_info': user_info,
                                                                       'address': address, }))
