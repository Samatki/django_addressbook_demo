# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from addressBookDemo.models import *

admin.site.register(Name)
admin.site.register(Country)
admin.site.register(TelephoneNumber)