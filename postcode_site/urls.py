from django.urls import path
from . import views

app_name = 'postcode_site'

urlpatterns = [
	path("", views.MainView.as_view(), name="index"),
	path("map/", views.MapView.as_view(), name="map"),
	]

