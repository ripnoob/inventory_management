from django.db import models
from accounts.models import CustomUser
from Inventory.models import Brand, Category
# Create your models here.

class Product(models.Model):

	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	price = models.FloatField()
	quantity = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


class Purchase(models.Model):

	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	