from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aparcamientos/$', 'app.views.aparcamientos'),
    url(r'^about/$', 'app.views.about'),
    url(r'^$', 'app.views.main'),
]
