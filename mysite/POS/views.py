from django.shortcuts import render
from .models import Login
import requests
# Create your views here.
def Home(request):
  if request.method == 'POST':
    email = request.POST.get("email")
    password = request.POST.get("password")
    username = request.POST.get("username")
    if Login.objects.filter(email=email).exists():
      print("User already exists")
      return render(request, "index.html", {"email": email})
    if email and password and username:
      login=Login(email=email,password=password)
      login.save()  
      return render(request,'home.html')
    else:
    
     error_message = "Please fill all the required fields"
     return render(request, "index.html", {'error_message': error_message})

  return render(request, "index.html")
def login(request):
  return render(request,"login.html")
  