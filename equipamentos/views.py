from django.shortcuts import render

def equipamentos_list(request):
	return render(request, 'equipamentos/equipamentos_list.html', {})