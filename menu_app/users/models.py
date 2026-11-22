from django.db import models

# Create your models here.
class Payment(models.IntegerChoices):
    EFT = 1, 'EFT'
    CREDIT_CARD = 2, 'Credit Card'
    PAYPAL = 3, 'Paypal'
    GOOGLE_PAY = 4, 'Google Pay'
    APPLE_PAY = 5, 'Apple Pay'
    PAYFAST = 6, 'Payfast'
    STRIPE = 7, 'Stripe'
    CASH = 8, 'Cash'

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    username = models.CharField(unique=True, max_length=200, null=False)
    email = models.EmailField(max_length=254, null=False)
    password = models.CharField(max_length=200, null=False)
    user_image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.IntegerField(choices=Payment.choices, default=Payment.CASH, null=False)

    def __str__(self):
        return self.username

