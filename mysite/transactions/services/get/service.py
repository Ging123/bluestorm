from django.core.paginator import Paginator
from django.http import HttpResponse

from django.core import serializers
from ...models import Transaction

class GetTransactionService:

  def get(self, page=None):
    page = self._validate_page(page)
    transactions = self._get_transaction_data(page)
    data = serializers.serialize('json', transactions)
    return HttpResponse(data, content_type='application/json')


  def _validate_page(self, page):
    if not page: return 1
    return int(page)
    

  def _get_transaction_data(self, page):
    limit = 20
    transactions = Transaction.objects.select_related('patient_id', 'pharmacy_id')
    paginator = Paginator(transactions, limit)
    return paginator.page(page).object_list