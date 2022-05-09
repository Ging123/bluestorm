from ...services.get.service import GetPatientsService
from .validation import GetPatientsValidation

from django.http import HttpResponse

def index(request):
  if request.method == 'GET': return _get(request)
  return HttpResponse(status=404)

  
def _get(request):
  patient = GetPatientsService()
  filter_data = GetPatientsValidation( request.GET )

  if not filter_data.is_valid(): return HttpResponse(
    list(filter_data.errors.as_json()),
    status=400
  )

  return patient.get( 
    request.GET.get('page'),
    request.GET.get('name'),
    request.GET.get('birthday'),
    request.GET.get('sort_by')
  )