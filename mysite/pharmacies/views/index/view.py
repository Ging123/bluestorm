from ...services.get.service import GetPharmaciesService
from .validation import GetPharmacyValidation

from django.http import HttpResponse

def index(request):
  if request.method == 'GET': return _get(request)
  return HttpResponse(status=404)


def _get(request):
  filter_data = GetPharmacyValidation( request.GET )
  pharmacies = GetPharmaciesService()

  if not filter_data.is_valid(): return HttpResponse(
    list(filter_data.errors.as_json()),
    status=400
  )

  return pharmacies.get( request.GET )