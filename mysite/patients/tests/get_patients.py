from ..services.get.service import GetPatientsService
from django.test import TestCase
from ..models import Patient

#python manage.py test patients.tests.get_patients

class GetPatientsTest(TestCase):

  patients = GetPatientsService()

  def test_get_patients(self):
    self.create_some_patients()
    res = self.patients.get()
  
    self.assertEqual(res.status_code, 200)
    self.assertTrue(res.content)


  def test_get_patients_by_name(self):
    self.create_some_patients()
    res = self.patients.get(name='Kim')
  
    self.assertEqual(res.status_code, 200)
    self.assertTrue(res.content)


  def test_get_patients_by_birthday(self):
    self.create_some_patients()
    res = self.patients.get(birthday='2000-02-03')
  
    self.assertEqual(res.status_code, 200)
    self.assertTrue(res.content)

  
  def test_get_patients_by_name_and_birthday(self):
    self.create_some_patients()
    res = self.patients.get(name='Jack', birthday='2000-02-03')
  
    self.assertEqual(res.status_code, 200)
    self.assertTrue(res.content)

  
  def create_some_patients(self):
    names = [ 'Jack', 'Billy', 'Kim', 'erick' ]
    last_name = ['kkkaa', 'aosa', 'soakf', 'psap' ]
    birthday = ['2000-02-03', '2004-05-21', '2013-03-16', '2018-12-03']
    index = 0

    for name in names:
      Patient.objects.create(
        name=name, 
        last_name=last_name[ index ], 
        birthday=birthday[ index ]
      )
      index+=1