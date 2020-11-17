from django.db import models

# Create your models here.
class encountered_url(models.Model):
	url = models.URLField(max_length=100)
	word = models.CharField(max_length=100)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.url