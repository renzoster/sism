from models import *

def globales(request):
	return {'proyecto':'SISM'}

def login_form(request):
	from django.contrib.auth.forms import AuthenticationForm
	form = AuthenticationForm()
	return {'login_form': form}

def recientes(request):
	canciones = Cancion.objects.order_by('-id')[:5]
	return {'recientes':canciones}

"""
def mostrarRecientes(request):
	data = [];
	generos = Genero.objects.order_by('?')[:3]
	for genero in generos:
		data.append({
			'genero' : genero.nombre,
			'canciones' : Cancion.objects.order_by('-id')[:5]
		})
	return {'recientes': data}
"""