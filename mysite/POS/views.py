from django.shortcuts import render
from .models import Signup
import requests
# Create your views here.
def Home(request):
  if request.method == 'POST':
    email = request.POST.get("email")
    password = request.POST.get("password")
    username = request.POST.get("username")
    if Signup.objects.filter(email=email).exists():
      print("User already exists")
      return render(request, "signup.html", {"email": email})
    if email and password and username:
      signup=Signup(email=email,password=password, username=username)
      signup.save()  
      return render(request,'home.html')
    else:
     error_message = "Please fill all the required fields"
     return render(request, "signup.html", {'error_message': error_message})

  return render(request, "signup.html")
def login(request):
  if request.method == 'POST':
    username = request.POST.get("username")
    if Signup.objects.filter(username=username).exists():
     return render(request, "home.html",{"uname": username})
    else:
     error = "User does not exist with this"
     return render(request,"login.html", {'login_error' : error, "uname": username} )
  return render(request,"login.html")
def signup(request):
  return render(request,"signup.html")