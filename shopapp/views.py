from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login

def signup(request):
      return render(request, 'signup.html')

def insert(request):
      return render(request, 'insert.php')

def main(request):
      category= Category.objects.filter(status=0)
      context={'category':category}
      return render(request, 'main.html', context)

def about(request):
      return render(request, 'about.html')

def cart(request):
      return render(request,'cart.html')

def my_acc(request):
      return render(request,'My_Acc.html')

def cartlogreq(request):
      return render(request,'cartlogreq.html')

def contact(request):
      return render(request, 'contact.html')

def collectionsview(request, slug):
      if(Category.objects.filter(slug=slug, status=0)):
            products=Product.objects.filter(category__slug=slug)
            category= Category.objects.filter(slug=slug).first()
            context= {'products':products, 'category':category }
            return render(request, "index.html", context)
      else:
            messages.warning(request, "No such category found")
            return redirect('main')

def productview(request, cate_slug, prod_slug):
      if(Category.objects.filter(slug=cate_slug, status=0)):
             if(Product.objects.filter(slug=prod_slug, status=0)):
                   products= Product.objects.filter(slug=prod_slug, status=0).first
                   context= {'products':products}
             else:
                   messages.error(request, "No such product found")
                   return redirect('main')
      else:
             messages.error(request, "No such category found")
             return redirect('main')
      return render(request, "view.html", context)



            
                   

            
           
     

