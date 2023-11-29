from django.db import models
from mart.models import Product
from accounts.models import Customer

# Create your models here.

class Sale(models.Model):
	
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	prod_price = models.FloatField()	
	extra_cost = models.FloatField(blank=True, null=True)
	paid = models.FloatField()
	quantity = models.IntegerField()
	is_refill = models.BooleanField()
	is_wholesale = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.product} - {self.customer.get_full_name()}'

	def total_cost(self):
		return (self.prod_price * self.quantity) + self.extra_cost



class Due(models.Model):

	sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
	due_amount = models.FloatField()
	is_paid = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.sale.customer.get_full_name} - {self.product} - {self.due_amount}'
