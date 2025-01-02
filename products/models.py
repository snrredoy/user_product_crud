from django.db import models
from customAbstractUser.models import CustomAbstractBaseUser

# Create your models here.
class Product(models.Model):

    owner = models.ForeignKey(CustomAbstractBaseUser , on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.CharField(max_length=255)



    def __str__(self):
        return self.name