# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *

from django.shortcuts import render

# Create your views here.
def display_data(request):
	# The addressBookDemoApp
	
	# uses name table as base for building dataset
	names = Name.objects.all()
	
	data = []
	
	# Builds array of dictionary from database for exporting to template
	for name in names:
		countries = name.country_set.all()
		numbers = name.telephonenumber_set.all()
		dataDict = {'name':name,'countries':countries,'telephoneNumbers':numbers}
		
		data.append(dataDict)
		
	context = {'data':data}


	return render(request,'addressBookDemo/display_data.html', context)