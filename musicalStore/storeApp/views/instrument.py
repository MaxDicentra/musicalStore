from django.http import HttpResponse
from storeApp.models.instrument import Instrument
from django.template import loader


def show_instrument(request, instrument_id):

    instrument = Instrument.objects.get(pk=instrument_id)
    template = loader.get_template('storeApp/instrument_page.html')
    context = {'instrument': instrument}
    return HttpResponse(template.render(context, request))
