from ..services.get.service import GetTransactionService
from pharmacies.models import Pharmacy

from patients.models import Patient
from django.test import TestCase

from ..models import Transaction

#python manage.py test transactions.tests.get_transactions

class GetTransactionService(TestCase):

  transactions = GetTransactionService()

  def test_get_transaction(self):
    self.create_some_transactions()
    res = self.transactions.get()

    self.assertEqual(res.status_code, 200)
    self.assertTrue(res.content)


  def create_some_transactions(self):
    patients = self.create_some_patients()
    pharmacies = self.create_some_pharmacies()

    quantities = [ 100, 23.4, 33, 152 ]
    dates = [ '2000-03-20', '2005-10-12', '2003-02-16', '2004-12-12' ]
    index = 0

    for quantity in quantities:
      Transaction.objects.create(
        patient_id=patients[index],
        pharmacy_id=pharmacies[index],
        quantity=quantity,
        date=dates[index]
      )
      index+=1


  def create_some_pharmacies(self):
    names = [ 'aksodkas', 'okfosa', 'okasokd', 'jifjasi' ]
    city = [ 'akosa', 'oasoa', 'osdas', 'kosaas' ]
    index = 0

    for name in names:
      Pharmacy.objects.create(name=name, city=city[index])
      index+=1
    
    return Pharmacy.objects.all()


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

    return Patient.objects.all()