from django.http import HttpResponse
from storeApp.models.instrument import Instrument
from django.template import loader


def show_catalog(request):

    instruments_list = Instrument.objects.all()
    template = loader.get_template('storeApp/catalog.html')
    context = {'instruments_list': instruments_list}
    return HttpResponse(template.render(context, request))
