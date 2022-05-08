from django.http import HttpResponse
from ...models import Patient

class GetPatientsService:

  def get(self, filters):
    filters = self._validate_filters(filters)

    patients = self._get_patients(
      filters['page'],
      filters['name'],
      filters['birthday'],
      filters['sort_by']
    )

    return HttpResponse(patients)


  def _validate_filters(self, filters):
    page = self._validate_page(filters.get('page'))
    sort_by = self._validate_sort_by(filters.get('sort_by'))

    return {
      'page':page,
      'name':filters.get('name'),
      'birthday':filters.get('birthday'),
      'sort_by':sort_by
    }

  
  def _validate_page(self, page):
    if not page: return 1
    return int(page)


  def _validate_sort_by(self, sort_by):
    if not sort_by: return 'name'
    if sort_by == 'name' or sort_by == 'birthday': return sort_by
    return 'name'


  def _get_patients(self, page, name, birthday, sort_by):
    limit = 20

    return (
      Patient
        .objects
        .filter(name=name, birthday=birthday)
        .order_by(sort_by)
        [ page:limit ]
    )