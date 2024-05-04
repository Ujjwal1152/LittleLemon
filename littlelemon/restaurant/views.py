from django.shortcuts import render
from .models import Menu
from .forms import BookingForm
from rest_framework import response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import menuSerializer
from rest_framework import generics

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'book.html',context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu': menu_data}
    return render(request,'menu.html',{'menu':main_data})
    
    
def display_menu_item(request,id=None):
    if id:
        menu_item = Menu.objects.get(id=id)
    else:
        menu_item = ""
    return render(request,'menu_item.html',{'menu_item':menu_item})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
