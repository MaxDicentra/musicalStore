from datetime import datetime, date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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
    # pdb.set_trace()
    return HttpResponseRedirect(reverse('profile'))


@login_required
def TestCard(request):
    if request.POST.get('confirm', False):
        card = request.POST['card']
        date = request.POST['date']
        if luhn(card):
            if CheckDate(request.POST['date']):
                return HttpResponseRedirect(reverse('create_order'))
            else:
                message = 'Сard expiration date is invalid'
                return render(request, 'card_conf.html', {'message': message})
        else:
            message = 'Сard  number is invalid'
            return render(request, 'card_conf.html', {'message': message})

    return render(request, 'card_conf.html')


def CheckDate(date_card):

    date_card = date_card.split('-')
    if int(date_card[1]) < datetime.today().month:
        if int(date_card[0]) < datetime.today().year:
            return False
    if int(date_card[0]) < datetime.today().year:
        return False
    return True


def luhn(ccn):
    c = [int(x) for x in ccn[::-2]]
    u2 = [(2*int(y))//10+(2*int(y))%10 for y in ccn[-2::-2]]
    return sum(c+u2)%10 == 0