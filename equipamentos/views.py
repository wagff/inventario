from django.shortcuts import render
from django.utils import timezone
from .models import Equipamentos

def equipamentos_list(request):
	equipamentos = Equipamentos.objects.all().order_by('patrimonio')
	return render(request, 'equipamentos/equipamentos_list.html', {'equipamentos' : equipamentos})