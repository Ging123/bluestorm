from django.core.paginator import Paginator
from django.http import HttpResponse

from ...models import Transaction
import json

class GetTransactionService:

  def get(self, page=None):
    page = self._validate_page(page)
    transactions = self._get_transaction_data(page)
    return HttpResponse(json.dumps(transactions))


  def _validate_page(self, page):
    if not page: return 1
    return int(page)
    

  def _get_transaction_data(self, page):
    limit = 20
    transactions = Transaction.objects.select_related('patient_id', 'pharmacy_id')
    print(transactions[0].patient_id.name)
    
    paginator = Paginator(transactions, limit)
    transactions_data = paginator.page(page).object_list

    return self._organizate_data(transactions_data)


  def _organizate_data(self, transactions):
    data = []

    for transaction in transactions:

      data.append({
        'patient_id': transaction.patient_id.id,
        'patient_name': transaction.patient_id.name,
        'patient_last_name': transaction.patient_id.last_name,
        'patient_birthday': transaction.patient_id.birthday.strftime('%d/%m/%Y'),
        'pharmacy_id': transaction.pharmacy_id.id,
        'pharmacy_name': transaction.pharmacy_id.name,
        'pharmacy_city': transaction.pharmacy_id.city,
        'transaction_id': transaction.id,
        'transaction_quantity': transaction.quantity,
        'transaction_date': transaction.date.strftime('%d/%m/%Y')
      })

    return data