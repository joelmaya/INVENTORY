from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django_google_maps import fields as map_fields
from django.conf import settings


CATEGORY_CHOICES = (
	('Super No 1','Super No 1'),
	('Premium No 1', 'Premium No 1'),
	)

CURRENCY_CHOICES = (
	('UGX','UGX'),
	('US$', 'US$'),
	)


SIZE_CATEGORY_CHOICES = (
	('2KG','2KG'),
	('5KG','5KG'),
	('10KG','10KG'),
	('25KG','25KG'),

	)

ORDER_STATUS_CHOICE = (
    ('delivered','delivered'),
    ('pending','pending'),
    ('canceled','canceled'),
	)


class product(models.Model):
	name = models.CharField(max_length=100)
	Quality = models.CharField(max_length=30, choices = CATEGORY_CHOICES)
	category = models.CharField(max_length=10, choices = SIZE_CATEGORY_CHOICES)
	quantity = models.IntegerField()
	price_ugx = models.DecimalField(max_digits=10, decimal_places=2)
	price_drc = models.DecimalField(max_digits=10, decimal_places=2)
	

	def __str__(self):
		return self.name + " | " + self.Quality + " | " + str(self.category) 

class order(models.Model):
	Distributor = models.ForeignKey(User, on_delete= models.CASCADE)
	product = models.ForeignKey(product, on_delete=models.CASCADE, default='maize|super No 1|2KG')
	date = models.DateTimeField(default = timezone.now)
	quantity = models.IntegerField()
	Issue_quantity = models.IntegerField(default=0, blank=True, null=True)
	delivery_address = models.TextField(null=True, blank=True)
	Telephone = models.CharField(max_length=30, blank= True, null = True)
	currency = models.CharField(max_length=3, choices = CURRENCY_CHOICES)


	def get_total(self):

		total = 0
		if self.currency == 'UGX':
			total = self.quantity * self.product.price_ugx
		elif self.currency == 'US$':
			total = self.quantity * self.product.price_drc
		else:
			print('please select currency!')
		return int(total)

	def __str__(self):
		return str(self.product)


	def get_absolute_url(self):

		return reverse('invent:home')

class Location(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)


    def __str__(self):
    	return self.address













