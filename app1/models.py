from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tickets(models.Model):
	owner=models.ForeignKey(User,on_delete=models.CASCADE)
	date_of_booking=models.DateTimeField(auto_now_add=True)
	status = 0

	source=models.CharField(max_length=20)
	destination=models.CharField(max_length=20)
	date_of_travel = models.DateField()

	def __str__(self):
		return str(self.date_of_booking)

