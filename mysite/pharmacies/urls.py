from .views.index.view import index as pharmacyViews
from django.urls import path

urlpatterns = [
  path('', pharmacyViews, name='get-pharmacies'),
]