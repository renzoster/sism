from django.shortcuts import render_to_response, get_object_or_404, render
from django.template.context import RequestContext
from models import *
import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def portada(request):
	canciones = Cancion.objects.order_by('-id')[:10]
	return render(request, "index.html", locals())

def logout(request):
    from django.contrib.auth import logout
    from django.http import HttpResponseRedirect

    logout(request)
    return HttpResponseRedirect('http://localhost:8000')

def buscar(request):
	q = request.GET['q']
	canciones = Cancion.objects.filter(nombre__icontains=q)
	return render(request, "buscar.html",{
		'q' : q,
		'canciones' : canciones
	})

def miMusica(request):
	canciones = Cancion.objects.filter(usuario = request.user)
	return render(request, "usuario/musica.html", locals())

def subirMusica(request):
	if request.POST:
		formulario = forms.CancionForm(request.POST, request.FILES)
		if formulario.is_valid():
			cancion = formulario.save(commit = False)
			cancion.usuario = request.user
			cancion.save()
			return HttpResponseRedirect("/")
	else:
		formulario = forms.CancionForm()
	return render_to_response("usuario/subir.html",context_instance=RequestContext(request,locals()))

def verMusica(request, id, url):
	cancion = get_object_or_404(Cancion, pk=id)
	return render_to_response("musica/simple.html",context_instance=RequestContext(request,locals()))
	#return render(request, "musica/simple.html", locals())