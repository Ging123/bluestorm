from .views.login.view import login as loginView
from .views.index.view import index as userViews
from django.urls import path

urlpatterns = [
  path('', userViews, name='create-user'),
  path('login', loginView, name='login-user')
]