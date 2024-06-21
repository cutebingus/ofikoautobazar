# Importy
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Definice URL cest
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]

# Přidání cest pro media a statické soubory pouze v režimu DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
