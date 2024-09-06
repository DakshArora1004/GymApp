
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
#any pattern not handled above will be handled by the following url pattern sent to REACT
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]