from django.db import models

# Create your models here.
class Laptops(models.Model):
    company=models.CharField(max_length=55)     # Laptops Company Names
    variant=models.CharField(max_length=55)     # Laptops Model Names
    ram=models.IntegerField()                   # RAM of Laptops
    rom=models.IntegerField()                   # ROM of Laptops
    price=models.IntegerField()                 # Price of Laptops



