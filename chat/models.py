from django.db import models

# Create your models here.

from django.db import models

# Esta es la sesion web de los que entran al proyecto
class Session(models.Model):
	user_name = models.CharField(max_length=100)
	start_date = models.DateField()
	user_avatar = models.IntegerField()
	
	def __str__(self):
		return self.user_name

