from django.contrib import admin
from .models import Product, Signup, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Signup)
admin.site.register(Category)

