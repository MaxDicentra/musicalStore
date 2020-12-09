"""musicalStore URL Configuration

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
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import include
from django_email_verification import urls as mail_urls
from storeApp.views import show_instrument, registration,  CreateOrder, DeleteFromCart, \
     profile, show_catalog, confirm_email, registration_submit, addToCart, \
    CancelOrder, CreateOrder, SearchWithFilters, SearchByName, Search, edit_profile, TestCard

from musicalStore import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', show_catalog, name='catalog'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile , name='edit_profile'),
    path('instrument/<int:instrument_id>', show_instrument, name='instrument'),
    path('catalog/', show_catalog, name='catalog'),
    path('search/', Search, name='search'),
    path('search_with_filters/', SearchWithFilters, name='search_with_filters'),
    path('search_by_name/', SearchByName, name='search_by_name'),
    path('registration/', registration, name='registration'),
    path('registration_submit/', registration_submit, name='registration_submit'),
    path('confirm_email/', confirm_email, name='confirm_email'),
    path('add_to_cart/<int:instrument_id>/<int:user_id>', addToCart, name='to_cart'),
    path('delete_from_cart/<int:cart_id>', DeleteFromCart, name='delete_from_cart'),
    path('cancel_order/', CancelOrder, name='cancel_order'),
    path('create_order/', CreateOrder, name='create_order'),
    path('confirm_by_email/<int:user_id>', confirm_email, name='confirm_by_email'),
    path('test_card', TestCard, name='test_card'),
]

urlpatterns += [path('accounts/', include('django.contrib.auth.urls')), ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += [path('email/', include(mail_urls))]
