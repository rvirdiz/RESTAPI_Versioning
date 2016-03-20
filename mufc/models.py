from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mufc(models.Model):
	name = models.CharField(max_length=30)
	created = models.DateTimeField(auto_now_add=True)
	skills = models.TextField(blank=True)
	country = models.CharField(max_length=20)
	age = models.IntegerField(blank=True, null=True)
	club = models.CharField(max_length=30, blank = True, null=True)

	class Meta:
		ordering = ('name',)