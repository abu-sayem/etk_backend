from django.db import models
from customers.models import Customer
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from django.utils import timezone

class Invoice(models.Model):
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)




class Transaction(models.Model):
    name = models.CharField(max_length=150)
    transaction_id = models.CharField(max_length=100)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    val_id = models.CharField(max_length=75)
    card_type = models.CharField(max_length=150)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_no = models.CharField(max_length=55, null=True)
    bank_tran_id = models.CharField(max_length=155, null=True)
    status = models.CharField(max_length=55)
    tran_date = models.DateTimeField()
    currency = models.CharField(max_length=10)
    card_issuer = models.CharField(max_length=255)
    card_brand = models.CharField(max_length=15)
    card_issuer_country = models.CharField(max_length=55)
    card_issuer_country_code = models.CharField(max_length=55)
    currency_rate = models.DecimalField(max_digits=10, decimal_places=2)
    verify_sign = models.CharField(max_length=155)
    verify_sign_sha2 = models.CharField(max_length=255)
    risk_level = models.CharField(max_length=15)
    risk_title = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name} - {self.amount}'
    

class Payment(models.Model):
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    ]
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unpaid')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.invoice} - {self.amount}'
    


class PaymentGatewaySettings(models.Model):
    store_id = models.CharField(max_length=500, blank=True, null=True)
    store_pass = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        verbose_name = "PaymentGatewaySetting"
        verbose_name_plural = "PaymentGatewaySettings"
        db_table = "paymentgatewaysettings"


    def __str__(self):
        return self.store_id


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.IntegerField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
        ('expired', 'Expired'),
    ]
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inactive')
    start_date = models.DateField()
    duration_months = models.IntegerField() 
    invoices = models.ManyToManyField(Invoice, related_name='subscriptions') 
    transactions = models.ManyToManyField(Transaction)

    def __str__(self):
        return f'{self.user} - {self.plan}'

    def calculate_end_date(self):
        return self.start_date + timedelta(days=30 * self.duration_months)

    def activate_subscription(self):
        self.status = 'active'
        self.save()

    def is_active(self):
        return self.status == 'active' and self.calculate_end_date() >= timezone.now().date()