from django.db import models

# Create your models here.
class Address(models.Model):
	parish = models.CharField(max_length = 20)
	city = models.CharField(max_length = 20)
	number = models.IntegerField()


class Employee(models.Model):
	e_id = models.IntegerField()
	name = models.CharField(max_length=200)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField(null=True)

	def __str__(self):
		return self.name

class Journey(models.Model):
	UNDERWAY = 'UNDERWAY'
	ENDED = 'ENDED'
	TOBEGIN = 'TOBEGIN'
	JOURNEY_STATES = (
		(UNDERWAY,'underway'),
		(ENDED,'ended'),
		(TOBEGIN,'tobegin'),
	)

	currentLocation = models.CharField(max_length = 20)
	destination = models.CharField(max_length = 20)
	noOfPeople = models.IntegerField()
	cost = models.DecimalField(max_digits=7,decimal_places=2)
	state = models.CharField(max_length=8,choices = JOURNEY_STATES, default = 'TOBEGIN')


class Vehicle(models.Model):
	carMake = models.CharField(max_length=50)
	carModel = models.CharField(max_length=50)
	carYear = models.CharField(max_length=4)
	carColor = models.CharField(max_length=20)
	licensePlate = models.CharField(max_length=10)


class Driver(Employee):
	AVAILABLE = 'AVAILABLE'
	UNAVAILABLE = 'UNAVAILABLE'

	DRIVER_STATE = (
		(AVAILABLE,'available'),
		(UNAVAILABLE,'unavailable')
	)

	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	trn = models.IntegerField()
	cellNum = models.CharField(max_length=10)
	state = models.CharField(max_length = 12,choices=DRIVER_STATE,default='AVAILABLE')
	currentJourney = models.ForeignKey(Journey, models.SET_NULL, blank=True,null=True)



class Customer(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	contact = models.CharField(max_length = 10)
	location = models.CharField(max_length = 10)
	destination = models.CharField(max_length = 20)
	noOfPassengers = models.IntegerField()


class DriverRequest(models.Model):
	APPROVED = 'APPROVED'
	DECLINED = 'DECLINED'
	REQUEST_STATUS = (
		(APPROVED,'approved'),
		(DECLINED,'declined')
	)

	journey = models.ForeignKey(Journey,on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	state = models.CharField(max_length=8,choices=REQUEST_STATUS,default='DECLINED')



