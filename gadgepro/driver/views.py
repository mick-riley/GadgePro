from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Customer, Driver


# Create your views here.
def index(request):
	return render(request,'driver/index.html')


class CustomerCreate(CreateView):
	model = Customer
	fields = ['first_name','last_name','contact','location','destination','noOfPassengers']

