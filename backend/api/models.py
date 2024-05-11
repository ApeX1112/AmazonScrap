from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class product(models.Model):
    name=models.CharField(max_length=300)
    url=models.URLField(unique=True)
    created=models.DateField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.name[:50]

class priceUpdate(models.Model):  #the price timeline of the product
    price=models.DecimalField(max_digits=9,decimal_places=2)
    date=models.DateTimeField(default=timezone.now)
    productName=models.ForeignKey(product,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return f"price at {self.date}"
    


class trackedProducts(models.Model):
    productname=models.CharField(max_length=300)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    url=models.URLField(unique=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s tracked product"





