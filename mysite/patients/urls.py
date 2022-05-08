from .views.index.view import index as patientViews
from django.urls import path

urlpatterns = [
  path('', patientViews, name='get-patients'),
]