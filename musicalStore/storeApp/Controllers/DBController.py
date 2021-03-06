import datetime

from storeApp.models import Address, Instrument, Order, Producer, Provider,\
    Storage, Type, UserConnection, Cart, OrderedInstr
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import pdb
from itertools import chain


class FullOrder:

    def __init__(self, order, instruments):
        self.order = order
        self.instruments = list(instruments)


class DBController(object):

    class UserKeys:
        ID = 'id'
        USERNAME = 'username'
        FIRST_NAME = 'first_name'
        LAST_NAME = 'last_name'
        PHONE = 'phone'
        PASSWORD = 'password'
        CONF_PASSWORD = 'conf_password'
        EMAIL = 'email'
        ADDRESS = 'address'
        COUNTRY = 'country'
        CITY_TYPE = 'city_type'
        CITY = 'city'
        STREET = 'street'
        FLAT = 'flat'
        GATE = 'gate'
        HOUSE = 'house'
        STREET_TYPE = 'street_type'
        INDEX = 'index'

    __instance = None

    def __new__(cls):
        if not DBController.__instance:
            cls.__instance = super(DBController, cls).__new__(cls)
        return cls.__instance

    def CreateUser(self, user_data):
        user = User.objects.create_user(username=user_data[self.UserKeys.USERNAME],
                                        first_name=user_data[self.UserKeys.FIRST_NAME],
                                        last_name=user_data[self.UserKeys.LAST_NAME],
                                        email=user_data[self.UserKeys.EMAIL],
                                        password=user_data[self.UserKeys.PASSWORD])
        address = self.CreateAddress(user_data)
        user.save()
        address.save()
        user_profile = UserConnection(phone=user_data[self.UserKeys.PHONE],
                                      id_user=user,
                                      id_address=address,
                                      confirmed=False)
        user_profile.save()

        return user

    def EditUser(self, user_data, user_id):
        user = User.objects.get(pk=user_id)
        user.username = user_data[self.UserKeys.USERNAME]
        user.first_name = user_data[self.UserKeys.FIRST_NAME]
        user.last_name = user_data[self.UserKeys.LAST_NAME]
        user.email = user_data[self.UserKeys.EMAIL]

        user_inf = UserConnection.objects.get(id_user=user.id)
        user_inf.phone = user_data[self.UserKeys.PHONE]

        self.EditAddress(user_data, user_inf)

        user.save()
        user_inf.save()

    def CreateAddress(self, user_data):
        address = Address(country=user_data[self.UserKeys.COUNTRY],
                          city_type=Address.CityType.CIT,
                          city=user_data[self.UserKeys.CITY],
                          street_type=Address.StreetType.STR,
                          street=user_data[self.UserKeys.STREET],
                          house=user_data[self.UserKeys.HOUSE],
                          gate=user_data[self.UserKeys.GATE],
                          flat=user_data[self.UserKeys.FLAT],
                          index=user_data[self.UserKeys.INDEX])
        address.save()
        return address

    def EditAddress(self, address_data, user_inf):
        address = user_inf.id_address

        address.country = address_data[self.UserKeys.COUNTRY]
        address.city_type = Address.CityType.CIT
        address.city = address_data[self.UserKeys.CITY]
        address.street_type = Address.StreetType.STR
        address.street = address_data[self.UserKeys.STREET]
        address.house = address_data[self.UserKeys.HOUSE]
        address.gate = address_data[self.UserKeys.GATE]
        address.flat = address_data[self.UserKeys.FLAT]
        address.index = address_data[self.UserKeys.INDEX]

        address.save()

    def AddToCart(self, id_instrument, user_id):

        instrument = Instrument.objects.get(pk=id_instrument)
        user = get_object_or_404(User, pk=user_id)

        cart = Cart(id_instrument=instrument, id_user=user)
        cart.save()

    def DeleteFromCart(self, cart_id):
        # pdb.set_trace()
        cart = Cart.objects.get(pk=cart_id)
        cart.delete()

    def GetUserCart(self, user_id):
        user = get_object_or_404(User, pk=user_id)
        instruments_con = Cart.objects.all().filter(id_user=user)

        total_price = 0
        instruments_list = []
        for i in range(len(instruments_con)):
            instruments_list.append(instruments_con[i].id_instrument)
            total_price += float(instruments_list[i].price)

        return instruments_list, instruments_con, total_price

    def GetOrders(self, user):
        orders = Order.objects.all().filter(id_user=user.id, is_active=True)
        result_list = []

        for order in orders:

            intruments = OrderedInstr.objects.all().filter(id_order=order.id)
            result_list.append(FullOrder(order, intruments))

        return result_list

    def GetCanceledOrders(self, user):
        orders = Order.objects.all().filter(id_user=user.id, is_active=False)
        result_list = []

        for order in orders:
            intruments = OrderedInstr.objects.all().filter(id_order=order.id)
            result_list.append(FullOrder(order, intruments))
        # pdb.set_trace()
        return result_list

    def CreateOrder(self, user):

        cart_instr = Cart.objects.all().filter(id_user=user.id)
        user_info = UserConnection.objects.get(id_user=user.id)
        order = Order(id_user=user, id_user_info=user_info, date=datetime.datetime.now().date(),
                      is_active=True, is_canceled=False)
        order.save()

        for cart in cart_instr:
            new_ord = OrderedInstr(id_instrument=cart.id_instrument, id_order=order)
            new_ord.save()
            cart.delete()
    # ввод данных карты

    def CancelOrder(self, order_id):
        order = Order.objects.get(pk=order_id)
        order.is_canceled = True
        order.is_active = False
        order.save()
    #     return money?

    def FinishOrder(self, order_id):
        order = Order.objects.get(pk=order_id)
        order.is_canceled = False
        order.is_active = False
        order.save()

    def GetInstruments(self, type, name, producer_country, producer, low_price, high_price, sort_by):

        instruments = Instrument.objects.all().filter(id_type=type.id)

        # pdb.set_trace()
        if producer:  # +++
            if producer.lower() != 'select':
                producer_obj = Producer.objects.get(name=producer)
                instruments = instruments.filter(id_producer=producer_obj)

        if producer_country:
            if producer_country.lower() != 'select':
                # pdb.set_trace()

                producers = Producer.objects.all().filter(id_address__country=producer_country)
                instruments = instruments.filter(id_producer__in=producers)

        # if high_price:
        #     instruments = instruments.filter(price__lte=high_price, price__gte=low_price)

        if name:
            instruments = instruments.filter(name__contains='name')

        if sort_by:
            if sort_by != 'select':
                if sort_by == 'high to low':
                    instruments = instruments.order_by('-price')
                elif sort_by == 'low to high':
                    instruments = instruments.order_by('price')

        return instruments

    def GetTypes(self):
        return Type.objects.all()

    def GetProdAndContr(self):
        producers_obj = Producer.objects.all()

        countries = []
        producers = []
        for prod in producers_obj:
            countries.append(prod.id_address.country)
            producers.append(prod.name)

        return producers, countries

    def GetProducer(self, name):
        return Producer.objects.get(name=name)

    def GetPrices(self, type):
        instruments = Instrument.objects.all().filter(id_type=type.id)
        instruments_max = instruments.order_by('price')[0]
        instruments_min = instruments.order_by('-price')[0]

        return instruments_max.price, instruments_min.price

    def GetUser(self, user_id):
        return User.objects.get(pk=user_id)

    def GetUserData(self, user_id,  user):

        user_info = UserConnection.objects.get(id_user=user_id)
        address = user_info.id_address
        return user_info, address

