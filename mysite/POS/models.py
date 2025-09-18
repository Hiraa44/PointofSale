from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price= models.DecimalField(max_digits=4, decimal_places=2)
    availability = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
class Category(models.Model):
    category_name = models.CharField(max_length=200)

class Signup(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=300, default="guest")
    
    #def __str__(self):
     #return(self.name)



