from django.contrib import admin
from .models import Driver, Customer, Journey, Address, Vehicle

# Register your models here.
admin.site.register(Address)
admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(Journey)