from utils.response import error_response
from django.http import HttpResponse

from libs.encrypy import Bcrypt
from decouple import config

from libs.token import Jwt
from ...models import User

import json

class LoginUserService:

  def login(self, email:str, password:str):
    user_found = self._get_user_by_email(email)
    if not user_found: return self._email_doesnt_exists_error()

    password_match = self._verify_if_password_match(
      password, 
      user_found.password
    )
    if not password_match: return self._wrong_password_error()

    token = self._login_user(user_found)
    return HttpResponse(json.dumps({ 'token':token }))

  
  def _get_user_by_email(self, email:str):
    user_found = User.objects.filter(email=email)
    user_was_found = len(user_found)

    if user_was_found: return user_found[0] 
    return False


  def _email_doesnt_exists_error(self):
    message = "this email doesn't exists"
    error = error_response(message, 'email')
    return HttpResponse(error, status=400)


  def _verify_if_password_match(self, text_password:str, hashed_password:str):
    bcrypt = Bcrypt()
    salt = config('PASSWORD_SALT')
    return bcrypt.match(text_password, hashed_password, salt)

  
  def _wrong_password_error(self):
    message = "wrong password"
    error = error_response(message, 'password')
    return HttpResponse(error, status=400)

  
  def _login_user(self, user):
    token = self._create_token(user)
    user.token = token

    user.save()
    return token


  def _create_token(self, user):
    jwt = Jwt()
    secret = config('LOGIN_TOKEN_SECRET')

    token = jwt.encode({ 'email':user.email }, secret)
    return token