from django.http import HttpResponse, HttpResponseRedirect
from storeApp.models.instrument import Instrument
from django.template import loader
from storeApp.Controllers.DBController import DBController
from django.urls import reverse

db = DBController()


def show_catalog(request):

    instruments_list = db.GetInstruments()
    template = loader.get_template('storeApp/catalog.html')
    context = {'instruments_list': instruments_list}
    return HttpResponse(template.render(context, request))


def search(request):
    pass


def addToCart(request, instrument_id, user_id):

    db.AddToCart(instrument_id, user_id)
    redirect_to = request.POST['next']
    return HttpResponseRedirect(redirect_to)
