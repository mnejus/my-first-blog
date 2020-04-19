from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_data = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	category = models.ForeignKey('Category', verbose_name='Kategoria', on_delete=models.SET_NULL, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name
