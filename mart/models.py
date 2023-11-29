from django.db import models
from accounts.models import CustomUser
from Inventory.models import Brand, Category, Supplier
# Create your models here.

class Product(models.Model):

	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	price = models.FloatField()
	quantity = models.IntegerField()
	is_refill = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
	
	def wholesale_price(self):
		pass


class Purchase(models.Model):

	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
	supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField()
	cost = models.FloatField()
	extra_cost = models.FloatField(blank=True, null=True)
	is_refill = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.product} {self.cost}'

	def single_prod_price(self):
		if self.cost and self.extra_cost:
			return (self.cost + self.extra_cost) / float(self.quantity)
		else:
			return 'N/A'
	def total_cost(self):
		return self.cost + self.extra_cost

	



class EmptySylinder(models.Model):
	
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
	brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product




class Return(models.Model):
	
	purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField()
	return_cost = models.FloatField()
	issue = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.purchase.product + '' + quantity

	def returned_product_price(self):
		if self.purchase and self.purchase.single_prod_price():
			return self.purchase.single_prod_price() * float(self.quantity)
		else:
			return 'N/A'
	
	def total_return_cost(self):
		if self.purchase and self.purchase.single_prod_price():
			product_price = self.purchase.single_prod_price() * float(self.quantity)
			return float(product_price) + self.return_cost
		else:
			return 'N/A'
