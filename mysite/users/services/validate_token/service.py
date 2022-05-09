from libs.encrypy import Bcrypt
from decouple import config

from ...models import User
from libs.token import Jwt

class ValidateUserTokenService:

  def token_is_valid(self, token):
    data = self._convert_token_to_data(token)
    if not data: return False 

    if not 'email' in data: return False
    return self._user_has_this_token(data['email'], token)

  
  def _convert_token_to_data(self, token):
    try:
      jwt = Jwt()
      secret = config('LOGIN_TOKEN_SECRET')

      data = jwt.decode(token, secret)
      return data
    except:
      return False


  def _user_has_this_token(self, email, token):
    user = User.objects.get(email=email)
    if not user: return False

    tokens_match = self._verify_if_tokens_match(token, user.token)
    return tokens_match

  
  def _verify_if_tokens_match(self, text_token, hash_token):
    salt = config('AUTH_TOKEN_SALT')
    bcrypt = Bcrypt()

    match = bcrypt.match(text_token, hash_token, salt)
    return match