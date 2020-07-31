from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
	path('', views.index, name = 'index' ),
	path('<int:adress_id>/', views.detail, name = 'detail'),
	path('<int:adress_id>/live_photo/', views.live_photo, name = 'live_photo'),
]	