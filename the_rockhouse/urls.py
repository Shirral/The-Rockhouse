from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('rocks.urls')),
    path('adoptions/', include('adoptions.urls')),
    path('profile/', include('userprofile.urls')),
    path('customisation/', include('customisation.urls')),
    path('gallery/', include('gallery.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
