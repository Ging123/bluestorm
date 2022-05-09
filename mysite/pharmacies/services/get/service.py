from django.core.paginator import Paginator
from django.http import HttpResponse

from django.core import serializers
from ...models import Pharmacy

class GetPharmaciesService:

  def get(self, page=None, name=None, city=None, sort_by=None):
    page = self._validate_page(page)
    sort_by = self._validate_sort_by(sort_by)
    pharmacies = self._get_pharmacies( page, name, city, sort_by )

    data = serializers.serialize('json', pharmacies)
    return HttpResponse(data, content_type='application/json') 


  def _validate_page(self, page):
    if not page: return 1
    return int(page)

  
  def _validate_sort_by(self, sort_by):
    if not sort_by: return 'name'
    if sort_by == 'name' or sort_by == 'city': return sort_by
    return 'name'


  def _get_pharmacies(self, page, name, city, sort_by):
    if name and city: 
      return self._get_pharmacies_by_name_and_city(page, name, city, sort_by)

    if name: return self._get_pharmacies_by_name(page, name, sort_by)
    if city: return self._get_pharmacies_by_city(page, city, sort_by)

    return self._get_all_pharmacies(page, sort_by)
      
    
  def _get_pharmacies_by_name_and_city(self, page, name, city, sort_by):
    limit = 20
    pharmacies = Pharmacy.objects.filter(name=name, city=city).order_by(sort_by)
    paginator = Paginator(pharmacies, limit)
    return paginator.page(page).object_list

  
  def _get_pharmacies_by_name(self, page, name, sort_by):
    limit = 20
    pharmacies = Pharmacy.objects.filter(name=name).order_by(sort_by)
    paginator = Paginator(pharmacies, limit)
    return paginator.page(page).object_list

  
  def _get_pharmacies_by_city(self, page, city, sort_by):
    limit = 20
    pharmacies = Pharmacy.objects.filter(city=city).order_by(sort_by)
    paginator = Paginator(pharmacies, limit)
    return paginator.page(page).object_list


  def _get_all_pharmacies(self, page, sort_by): 
    limit = 20
    pharmacies = Pharmacy.objects.filter().order_by(sort_by)
    paginator = Paginator(pharmacies, limit)
    return paginator.page(page).object_list