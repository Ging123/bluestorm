from utils.response import error_response
from django.http import HttpResponse

from libs.encrypy import Bcrypt
from decouple import config

from ...models import User

class CreateUserService:

  def create(self, email:str, password:str):
    email_already_exists = self._verify_if_email_already_exists(email)
    if email_already_exists: return self._email_already_exists_error()

    password = self._encrypt_password(password)
    self._save_user_in_database(email, password)
    return HttpResponse(status=201)

  
  def _verify_if_email_already_exists(self, email:str):
    user = User.objects.filter(email=email)
    email_already_being_used = len(user)
    return email_already_being_used

  
  def _email_already_exists_error(self):
    message = 'This email is already being used'
    error = error_response(message, 'email')
    return HttpResponse(error, status=400)


  def _encrypt_password(self, password:str):
    bcrypt = Bcrypt()
    salt = config('PASSWORD_SALT')
    return bcrypt.hash_value(password, salt)


  def _save_user_in_database(self, email:str, password:bytes):
    user = User(email=email, password=password)
    user.save()