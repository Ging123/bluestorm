from ..services.create.service import CreateUserService
from django.test import TestCase
from ..models import User

#python manage.py test users.tests.create_user

class CreateUserTest(TestCase):

  user = CreateUserService()
  email = 'jack@outlook.com'
  password = '123456789'
  
  def test_create_user(self):
    res = self.user.create(self.email, self.password)
    user = User.objects.get(email=self.email)

    status_code = res.status_code
    self.assertTrue(user)
    self.assertEqual(status_code, 201)

  
  def test_create_user_with_an_email_that_already_exists(self):
    self.user.create(self.email, self.password)
    res = self.user.create(self.email, self.password)

    status_code = res.status_code
    self.assertEqual(status_code, 400)