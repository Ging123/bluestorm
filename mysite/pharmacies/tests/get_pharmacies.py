from ..services.get.service import GetPharmaciesService
from django.test import TestCase
from ..models import Pharmacy

#python manage.py test pharmacies.tests.get_pharmacies

class GetPharmaciesTest(TestCase):

  pharmacy = GetPharmaciesService()

  def test_get_pharmacies(self):
    self.create_some_pharmacies()
    res = self.pharmacy.get()
  
    self.assertEqual(res.status_code, 200)
    self.assertTrue(res.content)

  
  def test_get_pharmacies_by_name(self):
    self.create_some_pharmacies()
    res = self.pharmacy.get(name='aksodkas')
  
    self.assertEqual(res.status_code, 200)
    self.assertTrue(res.content)

  
  def test_get_pharmacies_by_city(self):
    self.create_some_pharmacies()
    res = self.pharmacy.get(city='akosa')
  
    self.assertEqual(res.status_code, 200)
    self.assertTrue(res.content)

  
  def test_get_pharmacies_by_name_or_city(self):
    self.create_some_pharmacies()
    res = self.pharmacy.get(name='aksodkas', city='akosa')
  
    self.assertEqual(res.status_code, 200)
    self.assertTrue(res.content)

  
  def create_some_pharmacies(self):
    names = [ 'aksodkas', 'okfosa', 'okasokd', 'jifjasi' ]
    city = [ 'akosa', 'oasoa', 'osdas', 'kosaas' ]
    index = 0

    for name in names:
      Pharmacy.objects.create(name=name, city=city[index])
      index+=1