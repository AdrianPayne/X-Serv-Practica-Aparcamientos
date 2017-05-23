from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aparcamientos/(\d+)$', 'app.views.aparcamiento_individual'),
    url(r'^aparcamientos', 'app.views.aparcamientos_todos'),
    url(r'^about/$', 'app.views.about'),
    url(r'^$', 'app.views.main'),
    url(r'^login/$', 'app.views.auth'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^register/$','app.views.register'),
    url(r'^(.*)/XML$', 'app.views.usuarioXML'),
    url(r'^(.*)$', 'app.views.userpage'),
]
