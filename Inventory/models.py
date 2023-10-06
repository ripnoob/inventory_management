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


# class Product(models.Model):

# 	title = models.CharField(max_length=300, blank=False, null=False)
# 	stock_price = models.FloatField()
# 	selling_price = models.FloatField()
# 	image = models.ImageField(upload_to='product/')
# 	quantity = models.IntegerField()
# 	is_stock = models.BooleanField(default=True)
# 	category = models.ForeignKey(Category, on_delete=models.CASCADE)
# 	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
# 	is_refill = models.BooleanField(default=False)
# 	created_at = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return self.title

# 	class Meta:
# 		verbose_name_plural ="Product's"



# class Empty_Cylinder(models.Model):

# 	title = models.CharField(max_length=300, blank=False, null=False)
# 	price = models.FloatField()
# 	image = models.ImageField(upload_to='empty_cylinder/')
# 	quantity = models.IntegerField()
# 	category = models.ForeignKey(Category, on_delete=models.CASCADE)
# 	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
# 	created_at = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return self.title

# 	class Meta:
# 		verbose_name_plural = "Empty Cylinder's"


