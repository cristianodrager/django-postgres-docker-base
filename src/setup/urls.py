from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('scanner/', include('scanner.urls')),
    path('family/', include('family.urls')),
    path('grade/', include('grade.urls')),
]

