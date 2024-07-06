from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_app/', include('main_app.urls')),
    path('', RedirectView.as_view(url='/main_app/', permanent=True)),  # Redirige la raíz a main_app
    path('api/', include('main_app.api_urls')),
]
