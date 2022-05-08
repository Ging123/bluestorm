from django.http import HttpResponse
from ...models import Transaction

class GetTransactionService:

  def get(self, page):
    page = self._validate_page(page)
    transactions = self._get_transaction_data(page)
    return HttpResponse(transactions)


  def _validate_page(self, page):
    if not page: return 1
    return int(page)
    

  def _get_transaction_data(self, page):
    limit = 20

    return (
      Transaction
        .objects
        .select_related('patient_id', 'pharmacy_id')
        [ page:limit ]
    )