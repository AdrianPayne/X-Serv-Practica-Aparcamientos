from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aparcamientos/(\d+)$', 'app.views.aparcamiento_individual'),
    url(r'^aparcamientos', 'app.views.aparcamientos_todos'),
    url(r'^access$', 'app.views.accessparking'),
    url(r'^(.*)/XML$', 'app.views.userXML'),
    url(r'^about$', 'app.views.about'),
    url(r'^$', 'app.views.main'),
    url(r'^login/$', 'app.views.auth'),
    url(r'^static/css/index.css$','app.views.css'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^register/$','app.views.register'),
    url(r'^(.*)$', 'app.views.userpage'),
]
