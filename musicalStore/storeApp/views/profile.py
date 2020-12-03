from django.http import Http404
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'storeApp/profile.html')

