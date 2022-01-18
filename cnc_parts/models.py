from django.db import models



class Part(models.Model):
	name = models.CharField(max_length=50, verbose_name='Part name')
	image = models.ImageField(verbose_name='Image')
	description = models.TextField(verbose_name='Description', null=True)
	price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Price')

	def __str__(self):
		return self.name


class Shop(models.Model):
	title = models.CharField(max_length=50, verbose_name='Shop title')
	image = models.ImageField(verbose_name='Logo')
	parts = models.ManyToManyField(Part)

	def __str__(self):
		return self.title