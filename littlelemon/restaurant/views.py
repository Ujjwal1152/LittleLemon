from django.shortcuts import render
from .models import menu
from .forms import BookingForm
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
    pass