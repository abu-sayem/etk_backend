from django.shortcuts import render
from .models import SubscriptionPlan, Subscription, Invoice, Transaction
from django.utils import timezone
from dateutil.relativedelta import relativedelta


from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import transaction
from rest_framework import status

from django.http import HttpRequest

from .models import Transaction
from .sslcommerz import sslcommerz_payment_gateway
from .serializers import TransactionSerializer, SubscriptionPlanSerializer, InvoiceSerializer, SubscriptionSerializer


def PayView(request: HttpRequest) -> HttpResponse:
    return redirect(sslcommerz_payment_gateway(request))


class CheckoutSuccessView(APIView):
    model = Transaction

    def post(self, request, format=None):
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        payment_method = request.POST.get('payment_method')

        subscription_plan_serializer = SubscriptionPlanSerializer(data=request.data.get('subscription_plan'))
        invoice_serializer = InvoiceSerializer(data=request.data.get('invoice'))
        transaction_serializer = TransactionSerializer(data=request.data.get('transaction'))
        subscription_serializer = SubscriptionSerializer(data=request.data.get('subscription'))
        if all([serializer.is_valid() for serializer in [subscription_plan_serializer, invoice_serializer, transaction_serializer, subscription_serializer]]):
            try:
                with transaction.atomic():
                    subscription_plan = subscription_plan_serializer.save()
                    invoice = invoice_serializer.save()
                    transaction = transaction_serializer.save()
                    subscription = subscription_serializer.save()

                    subscription = Subscription.objects.get(user=request.user, status='pending')
                    subscription.status = 'active'
                    subscription.save()


                    return Response({'message': 'Payment Successful'}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    



class CheckoutFaildView(APIView):
    template_name = 'faild.html'

    def post(self, request, format=None):
        return Response({'message': 'Payment Failed'}, status=400)