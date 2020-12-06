from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from storeApp.Controllers.DBController import DBController

db = DBController()


@login_required
def profile(request):

    user_cart, cart_info = db.GetUserCart(request.user.id)
    show = 1
    empty = False
    if len(user_cart) == 0:
        empty = True

    if request.POST.get('show_orders', False):
        orders = db.GetOrders(request.user)
        show = 2
        return render(request, 'storeApp/profile.html', {
            'cart_info': None,
            'user_cart': None,
            'empty': True,
            'canceled_orders': None,
            'orders': orders,
            'show': show
        })
    elif request.POST.get('show_canceled_orders', False):
        canceled_orders = db.GetCanceledOrders(request.user)
        show = 3
        return render(request, 'storeApp/profile.html', {
            'cart_info': None,
            'user_cart': None,
            'empty': True,
            'canceled_orders': canceled_orders,
            'orders': None,
            'show': show,
        })

    return render(request, 'storeApp/profile.html', {
        'cart_info': cart_info,
        'user_cart': user_cart,
        'empty': empty,
        'canceled_orders': None,
        'orders': None,
        'show': show,
    })


@login_required
def DeleteFromCart(request, cart_id):
    db.DeleteFromCart(cart_id)
    redirect_to = request.POST['next']
    return HttpResponseRedirect(redirect_to)


