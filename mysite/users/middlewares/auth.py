from ..services.validate_token.service import ValidateUserTokenService
from utils.response import error_response
from django.http import HttpResponse

class AuthMiddleware:

  def __init__(self, get_response):
    self.get_response = get_response

  
  def __call__(self, request):
    response = self.get_response(request)
    return response

  
  def process_view(self, request, view_func, view_args, view_kwargs):
    url_name = request.resolver_match.url_name
    route_must_not_validated = self._verify_if_rote_must_be_validated(url_name) 
    
    if route_must_not_validated: return None
    return self._validate_auth_token(request)

  
  def _verify_if_rote_must_be_validated(self, url_name):
    routes_to_validate = ['get-patients', 'get-pharmacies', 'get-transaction']

    for route_name in routes_to_validate:
      if route_name == url_name: return False
    
    return True

  
  def _validate_auth_token(self, request):
    token = self._get_token(request.headers)
    if not token: return self._not_token_provider_error()

    token_is_valid = self._validate_token(token)
    if token_is_valid: return None
    
    return self._token_invalid_error()


  def _get_token(self, headers):
    if not 'authorization' in headers: return False
    return headers['authorization']

  
  def _not_token_provider_error(self):
    message = 'authorization token not sent'
    error = error_response(message, 'authorization')
    return HttpResponse(error, status=400)


  def _validate_token(self, token):
    user = ValidateUserTokenService()
    return user.token_is_valid(token)


  def _token_invalid_error(self):
    message = 'Invalid token'
    error = error_response(message, 'authorization')
    return HttpResponse(error, status=403)