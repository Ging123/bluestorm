from ..services.create.service import CreateUserService
from ..services.login.service import LoginUserService

from django.test import TestCase
from ..models import User

#python manage.py test users.tests.login

class LoginUserTest(TestCase):
  
  email = 'asd@gmail.com'
  password = '123456789'
  user = LoginUserService()

  def test_login(self):
    self.create_account()
    res = self.user.login( self.email, self.password )
    user = User.objects.get( email=self.email )

    self.assertEqual( res.status_code, 200 )
    self.assertTrue( user.token )

  
  def test_send_wrong_password(self):
    self.create_account()
    res = self.user.login( self.email, 'kkkas222' )
    self.assertEqual( res.status_code, 400 )


  def test_send_email_that_doesnt_exists(self):
    self.create_account()
    res = self.user.login( 'a', 'kkkas222' )
    self.assertEqual( res.status_code, 400 )


  def create_account(self):
    user = CreateUserService()
    user.create( self.email, self.password )