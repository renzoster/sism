# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.template import defaultfilters
import autoslug

class Genero(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100, blank=True)

	class Meta:
		verbose_name = 'Género'
		verbose_name_plural = 'Géneros'

	def __unicode__(self):
		return self.nombre

class Cancion(models.Model):
	nombre = models.CharField(max_length=100)
	url = models.SlugField(unique=True)
	genero = models.ForeignKey(Genero)
	usuario = models.ForeignKey(User)
	fechaCreacion = models.DateTimeField(auto_now_add=True)
	rutaArchivo = models.FileField(upload_to='musica', blank=True, verbose_name=u'Archivo')
	descripcion = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='imagenes', blank=True, null=True, verbose_name=u'Imagen')

	class Meta:
		verbose_name = 'Canción'
		verbose_name_plural = 'Canciones'

	def __unicode__(self):
		return unicode(self.nombre)

	def save(self, *args, **kwargs):
		self.url = defaultfilters.slugify(self.nombre)
		models.Model.save(self, *args, **kwargs)

	def get_absolute_url(self):
		return '%s' % (self.rutaArchivo.url)

"""
	def get_duration(self):
		import songdetails
		cancion = songdetails.scan(self.rutaArchivo)
		if cancion is not None:
			return cancion.duration
		else:
			return None
"""


class Playlist(models.Model):
	nombre = models.CharField(max_length=50)
	fechaCreacion = models.DateTimeField(auto_now_add=True)
	usuario = models.ForeignKey(User)
	descripcion = models.TextField(blank=True)
	cancion = models.ManyToManyField(Cancion)

	class Meta:
		verbose_name = 'Playlist'
		verbose_name_plural = 'Playlists'

	def __unicode__(self):
		return self.nombre