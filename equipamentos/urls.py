from django.urls import path
from . import views

urlpatterns = [
	path('', views.equipamentos_list, name='equipamentos_list'),
]