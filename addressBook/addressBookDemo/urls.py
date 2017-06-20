# Login for addressBookDemo app

from django.conf.urls import url

from . import views

urlpatterns = [
	# (Displays addressBookDemo)
	url(r'^$', views.display_data, name='display_data'),
]