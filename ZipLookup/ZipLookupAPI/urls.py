from django.urls import path
from .views import ZipLookupView

app_name = 'ZipLookupAPI'
urlpatterns = [
    path('', ZipLookupView.as_view()),
]