from .views.login.view import login as loginView
from .views.index.view import index as userView
from django.urls import path

urlpatterns = [
  path('', userView, name='create-user'),
  path('login', loginView, name='login-user')
]