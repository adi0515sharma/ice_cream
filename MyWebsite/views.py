from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")
    
def about(request):
    return render(request,"about.html")
def blog(request):
    return render(request,"blog.html")
def contact(request):
    return render(request,"contact.html")
def singlepost(request):
    return render(request,"singlepost.html")
def product(request):
    return render(request,"product.html")