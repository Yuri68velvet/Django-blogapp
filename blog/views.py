from django.shortcuts import render
from .models import Post
from .forms import ContactForm

# Create your views here.

#from django.http import HttpResponse




def home(request):
    context={'posts':Post.objects.all()}
        
    return render(request,'blog/home.html',context)
    
    #HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

def contact(request):
    form=ContactForm()
    return render(request,'blog/form.html',{'form':form})

