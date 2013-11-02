from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

#from forms import UploadFileForm
from django import forms
from django.forms import ModelForm
import models

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})

def login_form(request):
	from django.contrib.auth.forms import AuthenticationForm
	form = AuthenticationForm()
	return {'login_form': form}

class CancionForm(ModelForm):
    class Meta:
        model = models.Cancion
        exclude = ("url", "usuario", "fechaCreacion",)

    