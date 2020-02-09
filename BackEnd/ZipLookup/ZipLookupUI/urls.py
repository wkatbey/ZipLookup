from django.urls import path
from .views import UIView

app_name = 'ZipLookupUI'
urlpatterns = [
    path('', UIView.as_view()),
]
