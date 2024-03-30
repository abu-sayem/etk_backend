from rest_framework import serializers
from .models import Invoice, Transaction, Payment, PaymentGatewaySettings, SubscriptionPlan, Subscription

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentGatewaySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentGatewaySettings
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    plan = SubscriptionPlanSerializer()
    invoices = InvoiceSerializer(many=True)
    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Subscription
        fields = '__all__'