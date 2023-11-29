from django.db import models

# Create your models here.

class Category(models.Model):

	weight = models.CharField(max_length=100, null=False, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.weight)

	class Meta:
		verbose_name_plural='Categories'


class Brand(models.Model):

	name = models.CharField(max_length=200, blank=False, null=False)
	email = models.EmailField(blank=False, null=False)
	phone = models.CharField(max_length=18)
	address = models.CharField(max_length=200, default='Unknown')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Supplier(models.Model):

	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	contact_name = models.CharField(max_length=200)
	address = models.CharField(max_length=200, blank=True, null=True)
	phone = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.contact_name} - {self.brand}'


