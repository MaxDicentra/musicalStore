"""musicalStorePr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from storeApp.views import show_instrument, registration, \
     profile, show_catalog, confirm_email, registration_submit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_catalog, name='catalog'),
    path('profile/', profile, name='profile'),
    path('instrument/<int:instrument_id>', show_instrument, name='instrument'),
    path('catalog/', show_catalog, name='catalog'),
    # path('login_submit', log_in_submit, name='log_in_submit'),
    path('registration', registration, name='registration'),
    path('registration_submit', registration_submit, name='registration_submit'),
    path('confirm_email', confirm_email, name='confirm_email'),
]

urlpatterns += [path('accounts/', include('django.contrib.auth.urls')), ]
