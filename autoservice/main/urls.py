from django.urls import path
from main.views import *

urlpatterns = [
    path('', index, name='home'),
    path('service', service, name='service'),
    path('contact', contact, name='contact'),
    path('registr',registr, name='registr'),
]