from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ZipLookupUI.urls')),
    path('zip-lookup/', include('ZipLookupAPI.urls')),
]
