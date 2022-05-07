from ...services.create.service import CreateUserService
from .validation import CreateUserForm
from django.http import HttpResponse
import json

def index(request):
  if request.method == 'POST': return _post(request)
  return HttpResponse(status=404)


def _post(request):
  request_data = json.loads(request.body)
  user = CreateUserForm(request_data)
  newUser = CreateUserService()

  if not user.is_valid(): return HttpResponse(
    list(user.errors.as_json()),
    status=400
  )

  return newUser.create(
    user.data['email'], 
    user.data['password']
  )