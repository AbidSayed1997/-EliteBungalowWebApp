from django.shortcuts import render , redirect
from . forms import ContactForm,LoginForm,RegistrationForm
from . models import BunglowModel,DisplayLocation, Resort
from django.contrib.auth import authenticate,login,logout

# from django.views import View

# Create your views here.


def register(request):
    
    form = RegistrationForm()
    
    form1 = RegistrationForm(request.POST)
    
    if form1.is_valid():
        
        form1.save()
        
        return redirect('home')
        
    return render(request,'register.html',{'form':form})


def home(request):
    
    data = DisplayLocation.objects.all()
    r = Resort.objects.all()
    
    form = LoginForm()
    
    con = {'data':data,'r':r,'form':form}
    
    return render(request,'home.html',con)

def services(request):
    form = LoginForm()

    return render(request,'services.html',{"form":form})

def about(request):
    form = LoginForm()
    
    return render(request,'about.html',{"form":form})
    
def contact(request):
    
    if request.POST:
        
        data = ContactForm(request.POST)
        
        if data.is_valid():
            
            data.save()
            return redirect('home')
        
        return redirect('contact')

    else:
        
        form1 = ContactForm()
        form = LoginForm()
        
        return render(request,'contact.html',{'form1':form1,'form':form})


def bunglow(request,l_name):    
        
    data = DisplayLocation.objects.get(location_name = l_name)
    data2 = BunglowModel.objects.filter(location = data)

    form = LoginForm()

    context = {'data2':data2,'data':data,'form':form}
        
    return render(request,'bunglow.html',context)


def bunglow_details(request,pk):
    
    id = BunglowModel.objects.get(id = pk)
    
    # desc = BunglowModel.objects.get(desc=id)
            
    # desc = desc.split(".")
    # print(desc)
    
    
    
    # id = BunglowModel.objects.all()
        
    context = {'id':id}
    # print(details)
    
    return render(request,'details.html',context)
    
    
def resort(request):
    
    form = LoginForm()
    
    
    return render(request,'resort.html',{"form":form})



