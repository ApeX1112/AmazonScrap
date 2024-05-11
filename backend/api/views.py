from django.shortcuts import render , redirect
from .models import priceUpdate,product ,trackedProducts
from django.http import HttpResponse
from scrapper import amazon_scrapper
from .forms import MyUserCreationForm , TrackingForm
from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def home(request):
    q=request.GET.get('q')
    if q:

        products=product.objects.filter(name__icontains=q)

    else:
        products=product.objects.all()

    context={'products':products}
    return render(request,'Home.html',context)


def showProduct(request,pk):
    prod=product.objects.get(pk=pk)
    price_updates=priceUpdate.objects.filter(productName=prod).order_by('date')

    context={'item':prod , 'prices':price_updates}
    return render(request,'item.html',context)

@login_required
def tracking(request):
    tracked_prods=trackedProducts.objects.filter(user=request.user)
    if request.method=='POST':
        form=TrackingForm(request.POST)
        
        if form.is_valid():
            url=form.cleaned_data['url']
            if request.user.is_authenticated:
                scrap_url=amazon_scrapper.product_scrapper(url)
                name=scrap_url.get_title()

                product.objects.create(name=name,url=url)

                instance=form.save(commit=False)
                instance.productname=name
                instance.user=request.user
                form.save()
                return redirect('track')
            else:
                form.add_error(None,"You must be logged in ")
        
    else:
        form=TrackingForm()
    return render(request,'tracking_page.html',{'form':form,'trakedprods':tracked_prods})

def register(request):
    
    if request.method == 'POST':
        
        form=MyUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form = MyUserCreationForm()
    return render(request,'register.html',{'form':form})


def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
                
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def LogoutUser(request):
    logout(request)

    return redirect('home')