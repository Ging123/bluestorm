from django.http import HttpResponse
from ...models import Pharmacy

class GetPharmaciesService:

  def get(self, filters):
    filters = self._validate_filters(filters)
    
    pharmacies = self._get_pharmacies(
      filters['page'],
      filters['name'],
      filters['city'],
      filters['sort_by']
    )

    return HttpResponse(pharmacies)


  def _validate_filters(self, filters):
    page = self._validate_page(filters.get('page'))
    sort_by = self._validate_sort_by(filters.get('sort_by'))

    return {
      'page':page,
      'name':filters.get('name'),
      'city':filters.get('city'),
      'sort_by':sort_by
    }


  def _validate_page(self, page):
    if not page: return 1
    return int(page)

  
  def _validate_sort_by(self, sort_by):
    if not sort_by: return 'name'
    if sort_by == 'name' or sort_by == 'city': return sort_by
    return 'name'


  def _get_pharmacies(self, page, name, city, sort_by):
    limit = 20

    return (
      Pharmacy
        .objects
        .filter(name=name, city=city)
        .order_by(sort_by)
        [ page:limit ]
    )