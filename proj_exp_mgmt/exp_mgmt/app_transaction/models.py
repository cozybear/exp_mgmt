from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.


class Balance(models.Model):

    category_choices = [("STN", "Stationary"),
                        ("OFF", "Office"),
                        ("MED", "Medical"),
                        ("HOS", "House"),
                        ("KIT", "Kitchen"),
                        ("DAR", "Dairy"),
                        ("PER", "Personal"),
                        ]

    transaction = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')
    category = models.CharField(max_length=25,choices=category_choices)

    def __str__(self):
        return self.category