from ...services.login.service import LoginUserService
from .validation import LoginUserForm
from django.http import HttpResponse
import json

def login(request):
  if request.method == 'POST': return _post(request)
  return HttpResponse(status=404)


def _post(request):
  request_data = json.loads(request.body)
  login_data = LoginUserForm(request_data)
  user = LoginUserService()

  if not login_data.is_valid(): return HttpResponse(
    list(login_data.errors.as_json()),
    status=400
  )
  
  return user.login(
    login_data.data['email'],
    login_data.data['password']
  )