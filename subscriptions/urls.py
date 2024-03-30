from django.urls import path
from .views import *


app_name = "donationapp"

urlpatterns = [
    path('donate/', PayView, name='donate'),
    path('payment/success/', CheckoutSuccessView.as_view(), name='success'),
    path('payment/faild/', CheckoutFaildView.as_view(), name='faild'),

]