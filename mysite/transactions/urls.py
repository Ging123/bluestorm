from .views.index.view import index as transactionViews
from django.urls import path

urlpatterns = [
  path('', transactionViews, name='get-transaction')
]