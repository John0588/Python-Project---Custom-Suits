from django.shortcuts import render, redirect
from .forms import signInForm, signUpForm
from .models import user
from django.core import serializers
# from django.core.mail import send_mail
import json



# Home
def home(request):
  # try:
  #   homeData = json.loads(request.session['user'])
  #   return render(request, 'home.html', {'user': homeData[0]})

  # except:
  #   return redirect('/signIn')

   # Need to delete
 return render(request, 'customSuits/home.html')

# About
def about(request):
  # try:
  #   aboutData = json.loads(request.session['user'])
  #   return render(request, 'about.html', {'user': aboutData[0]})

  # except:
  #   return redirect('/signIn')

#    Need to delete
 return render(request, 'customSuits/about.html')

# ContactUs
def contactUs(request):
  if request.method == 'POST':
    firstName = request.POST['fName']
    lastName = request.POST['lName']
    email = request.POST['email']
    message = request.POST['message']

    return render(request, 'customSuits/contactUs.html', {'fName': firstName, 'lName' : lastName })

  else:
    return render(request, 'customSuits/contactUs.html', {})

# Services
def services(request):
  # try:
  #   servicesData = json.loads(request.session['user'])
  #   return render(request, 'contactUs.html', {'user': servicesData[0]})

  # except:
  #   return redirect('/signIn')

   # Need to delete
 return render(request, 'customSuits/services.html')

# Sign Up
def signUp(request):
  if request.method == 'POST':
    submitted_form = signUpForm(request.POST)
    if submitted_form.is_valid():
      fName = submitted_form.cleaned_data['fName']
      lName = submitted_form.cleaned_data['lName']
      email = submitted_form.cleaned_data['email']
      password = submitted_form.cleaned_data['password']
      user_Costumer = user.objects.filter(email = email)

      if user_Costumer:
          note = "Account is already exist, Please Sign In!"
          user_Costumer = serializers.serialize('json',user_Costumer)
          form = signUpForm
          return render(request, 'customSuits/signUp.html', {'signUpForm': form, 'note':note})
      else:
        costumerData = user(firstName = fName, lastName = lName, email = email, password = password)
        costumerData.save()
        note = "Congratualations! You are officially User"
        form = signUpForm()
        return render(request, 'customSuits/signUp.html', {'signUpForm':form, 'note':note})

  else:
    form = signUpForm()
    return render(request, 'customSuits/signUp.html', {'signUpForm':form})

# Sign In
def signIn(request):
  if request.method == 'POST':
    submitted_form = signInForm(request.POST)
    if submitted_form.is_valid():   
      email = submitted_form.cleaned_data['email']
      password = submitted_form.cleaned_data['password']
      
      user_Costumer = user.objects.filter(email = email, password = password)
      if user_Costumer:
          user_Costumer = serializers.serialize('json', user_Costumer)
          request.session['user'] = user_Costumer
          return redirect('/')

      else:
          note = "Your Email and Password is not correct!"
          form = signInForm
          return render(request, 'customSuits/signIn.html', {'signInForm': form, 'note':note})

  else:
    form = signInForm()
    return render(request, 'customSuits/signIn.html', {'signInForm': form})

# Item
def item(request):
  # try:
  #   itemData = json.loads(request.session['user'])
  #   return render(request, 'item.html', {'user': itemData[0]})

  # except:
  #   return redirect('/signIn')

  # Need to delete
 return render(request, 'customSuits/item.html')

#  Cart
def cart(request):
  # try:
  #   cartData = json.loads(request.session['user'])
  #   return render(request, 'cart.html', {'user': cartData[0]})

  # except:
  #   return redirect('/signIn')

  # Need to delete
 return render(request, 'customSuits/cart.html')


 
