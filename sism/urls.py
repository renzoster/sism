from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	#url(r'^api/', include(router.urls)),
    # Examples:
    url(r'^$', 'musica.views.portada', name='portada'),
    url(r'^cuenta/entrar/$', 'django.contrib.auth.views.login', {'template_name': 'usuario/login.html'}),
    url(r'^cuenta/salir/$', 'musica.views.logout', name='logout'),
    url(r'^buscar/$', 'musica.views.buscar', name='buscar'),

    url(r'^cuenta/musica/$', 'musica.views.miMusica', name='miMusica'),
    url(r'^cuenta/subir/$', 'musica.views.subirMusica', name='subirMusica'),

    url(r'^cuenta/perfil/$', 'usuario.views.perfil', name='perfil'),

    url(r'^musica/(?P<id>[\d]+)/(?P<url>[^/]+)/$', 'musica.views.verMusica', {}, name='verMusica'),
    # url(r'^sism/', include('sism.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)