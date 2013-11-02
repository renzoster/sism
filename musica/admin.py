from django.contrib import admin
from models import *

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

class CancionAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'genero', 'usuario', 'fechaCreacion')

admin.site.register(Genero, GeneroAdmin)
admin.site.register(Cancion, CancionAdmin)
admin.site.register(Playlist)