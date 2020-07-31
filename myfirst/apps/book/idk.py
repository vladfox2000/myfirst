from django.urls import path
from . import views

urlpatterns = [
	path('', views.index1, name = 'index1'),
	path('add/', views.add_person, name = 'add_person'),
]	