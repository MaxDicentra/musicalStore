from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from storeApp.Controllers.DBController import DBController
import pdb

db = DBController()


@login_required
def CancelOrder(request):

    order_id = request.POST.get('order_id', None)
    # pdb.set_trace()
    db.CancelOrder(order_id)
    redirect_to = request.POST['next']
    return HttpResponseRedirect(redirect_to)


@login_required
def CreateOrder(request):
    db.CreateOrder(request.user)
    redirect_to = request.POST['next']
    return HttpResponseRedirect(redirect_to)
