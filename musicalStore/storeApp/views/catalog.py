from django.http import HttpResponse, HttpResponseRedirect
from storeApp.models.instrument import Instrument
from django.template import loader
from storeApp.Controllers.DBController import DBController
from django.urls import reverse
import pdb

db = DBController()


def show_catalog(request):

    types = db.GetTypes()
    show_types = True
    if request.POST.get('show_types', True) is not True:

        type = GetType(request, types)
        producers, countries = db.GetProdAndContr()
        highest_price, lowest_price = db.GetPrices(type)
        sorts = ['high to low', 'low to high']

        if request.POST.get('filter', False):

            sort_by = request.POST.get('sort_by', 'select')
            # pdb.set_trace()
            producer_country = request.POST.get('countries_s', 'select')
            producer = request.POST.get('producers_s', 'select')
            low_price, high_price = GetPriceLimits(request, highest_price, lowest_price)
            name = request.POST.get('name', None)

            instruments_list = db.GetInstruments(type, name, producer_country, producer, low_price, high_price, sort_by)
            template = loader.get_template('storeApp/catalog.html')
            context = {'instruments_list': instruments_list,
                       'show_types': False,
                       'type': type,
                       'producer': producer,
                       'producer_country': producer_country,
                       'low_limit': low_price,
                       'high_limit': high_price,
                       'sort_by': sort_by,
                       'countries': countries,
                       'producers': producers,
                       'highest_price': highest_price,
                       'lowest_price': lowest_price,
                       'sorts': sorts,
                       }
            return HttpResponse(template.render(context, request))

        instruments_list = db.GetInstruments(type, None, None, None, None, None, None)
        template = loader.get_template('storeApp/catalog.html')
        context = {'instruments_list': instruments_list,
                   'show_types': False,
                   'type': type,
                   'producer': request.POST.get('producers_s', 'select'),
                   'producer_country': request.POST.get('countries_s', 'select'),
                   'countries': countries,
                   'producers': producers,
                   'low_limit': lowest_price,
                   'high_limit': highest_price,
                   'sort_by': request.POST.get('sort_by','select'),
                   'highest_price': highest_price,
                   'lowest_price': lowest_price,
                   'sorts': sorts,
                   }
        return HttpResponse(template.render(context, request))

    template = loader.get_template('storeApp/catalog.html')
    context = {'instruments_list': None,
               'types': types,
               'show_types': show_types,
               }
    return HttpResponse(template.render(context, request))


def Search(request):

    redirect_to = request.POST['next']
    return HttpResponseRedirect(redirect_to)


def SearchWithFilters(request):

    redirect_to = request.POST['next']
    return HttpResponseRedirect(redirect_to)


def SearchByName(request):

    redirect_to = request.POST['next']
    return HttpResponseRedirect(redirect_to)


def addToCart(request, instrument_id, user_id):

    db.AddToCart(instrument_id, user_id)
    redirect_to = request.POST['next']
    return HttpResponseRedirect(redirect_to)


def GetType(request, types):

    for type in types:
        if request.POST.get(type.inst_type, False):
            # pdb.set_trace()
            return type
    return None


def GetPriceLimits(request, highest_price, lowest_price):

    low_limit = request.POST.get('low_limit', lowest_price)
    high_limit = request.POST.get('high_limit', highest_price)

    return low_limit, high_limit

