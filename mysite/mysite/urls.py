from django.urls import path, include

urlpatterns = [
  path('users/', include('users.urls')),
  path('patients/', include('patients.urls')),
  path('pharmacies/', include('pharmacies.urls')),
  path('transactions/', include('transactions.urls'))
]