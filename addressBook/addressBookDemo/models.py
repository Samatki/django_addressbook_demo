# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Name(models.Model):
    # List of users in address book
	text = models.CharField(max_length=50)
	date_added = models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
	    return self.text
		
class Country(models.Model):
	text = models.CharField(max_length = 20)
	names = models.ManyToManyField(Name)
		
	class Meta:
	# Renames 'Countrys' to 'Countries'
		verbose_name_plural = 'countries'
		
	def __str__(self):
		return self.text



class TelephoneNumber(models.Model):
	text=models.CharField(max_length=12)
	name = models.ForeignKey(Name)
	
	def __str__(self):
		return self.text