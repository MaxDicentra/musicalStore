from django.contrib import admin
from .models import Address, Instrument, Order, Producer, Provider, Storage, Type, UserConnection

admin.site.register(Address)
admin.site.register(Instrument)
admin.site.register(Order)
admin.site.register(Provider)
admin.site.register(Producer)
admin.site.register(Storage)
admin.site.register(Type)
admin.site.register(UserConnection)




