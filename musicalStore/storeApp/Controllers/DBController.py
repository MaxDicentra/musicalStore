from django.contrib.auth.models import User
from storeApp.models import Address, UserConnection
from django.db import models


class DBController:

    class UserKeys:
        USERNAME = 'username'
        FIRST_NAME = 'first_name'
        LAST_NAME = 'last_name'
        PHONE = 'phone'
        PASSWORD = 'password'
        CONF_PASSWORD = 'conf_password'
        EMAIL = 'email'
        ADDRESS = 'address'

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

    def EditUser(self):
        pass

    def CreateAddress(self):
        id = 1
        return Address.objects.get(pk=id)
