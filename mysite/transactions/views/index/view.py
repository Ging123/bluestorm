from ...services.get.service import GetTransactionService
from .validation import GetTransactionValidation
from django.http import HttpResponse

def index(request):
  if request.method == 'GET': return _get(request)
  return HttpResponse(status=404)


def _get(request):
  transactions = GetTransactionService()
  filter_data = GetTransactionValidation( request.GET )

  if not filter_data.is_valid(): return HttpResponse(
    list(filter_data.errors.as_json()),
    status=400
  )

  return transactions.get(request.GET.get('page'))