from django.shortcuts import render_to_response, get_object_or_404, render
from django.template.context import RequestContext
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def perfil(request):
	return render(request, "usuario/perfil.html", locals())