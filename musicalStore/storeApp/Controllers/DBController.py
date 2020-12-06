import datetime

from django.conf import settings
from storeApp.models import Address, Instrument, Order, Producer, Provider,\
    Storage, Type, UserConnection, Cart, OrderedInstr
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import pdb


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
        address = self.CreateAddress()
        user.save()
        address.save()
        user_profile = UserConnection(phone=user_data[self.UserKeys.PHONE],
                                      id_user=user,
                                      id_address=address,
                                      confirmed=False)
        user_profile.save()

    def EditUser(self, user_data, address_data):
        user = User.objects.get(pk=user_data[self.UserKeys.ID])
        user.username = user_data[self.UserKeys.USERNAME]
        user.first_name = user_data[self.UserKeys.FIRST_NAME]
        user.last_name = user_data[self.UserKeys.LAST_NAME]
        user.email = user_data[self.UserKeys.EMAIL]
        user.password = user_data[self.UserKeys.PASSWORD]

        user_inf = UserConnection.objects.get(id_user=user.id)
        user_inf.phone = user_data[self.UserKeys.PHONE]

        user.save()
        user_inf.save()

    def CreateAddress(self):
        id = 1
        return Address.objects.get(pk=id)

    def EditAddress(self, address_data, user_id):
        user = User.objects.get(pk=user_id)
        user_inf = UserConnection.objects.get(id_user=user.id)
        address = Address.objects.get(pk=user_inf.id_address)

    #     change data

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

        instruments_list = []
        for i in range(len(instruments_con)):
            instruments_list.append(instruments_con[i].id_instrument)

        return instruments_list, instruments_con

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

    def GetInstruments(self):
        return Instrument.objects.all()
