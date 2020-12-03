# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
# from django.template import loader
# from django.urls import reverse
# from storeApp.Controllers.DBController import DBController
#
#
# def log_in(request):
#
#     return HttpResponse(render(request, 'storeApp/login_page.html'))
#
#
# def log_in_submit(request):
#     # check if passwords match
#     try:
#         # get user through DB
#         user_email = request.POST['email']
#         user_password = request.POST['password']
#         # user_password_hash =
#         user_id = 1
#         pass
#     except KeyError:
#         return render(request, 'storeApp/registration.html', {
#             'error_message': "Something is wrong!",
#         })
#     else:
#         # save new_user data to DB and send confirmation message to email
#         return HttpResponseRedirect(reverse('profile', args=(user_id, )))
#
