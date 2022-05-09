from django.core.paginator import Paginator
from django.http import HttpResponse

from django.core import serializers
from ...models import Patient

class GetPatientsService:

  def get(self, page=None, name=None, birthday=None, sort_by=None):
    page = self._validate_page(page)
    sort_by = self._validate_sort_by(sort_by)
    patients = self._get_patients( page, name, birthday, sort_by )

    data = serializers.serialize('json', patients)
    return HttpResponse(data, content_type='application/json') 

  
  def _validate_page(self, page):
    if not page: return 1
    return int(page)


  def _validate_sort_by(self, sort_by):
    if not sort_by: return 'name'
    if sort_by == 'name' or sort_by == 'birthday': return sort_by
    return 'name'


  def _get_patients(self, page, name, birthday, sort_by):
    if name and birthday:
      return self._get_patients_by_name_and_birthday(page, name, birthday, sort_by)
      
    if name: return self._get_patients_by_name(page, name, sort_by)
    if birthday: return self._get_patients_by_birthday(page, birthday, sort_by)

    return self._get_all_patients(page, sort_by)

  
  def _get_patients_by_name_and_birthday(self, page, name, birthday, sort_by):
    limit = 20
    patients = Patient.objects.filter(name=name, birthday=birthday).order_by(sort_by)
    paginator = Paginator(patients, limit)
    return paginator.page(page).object_list


  def _get_patients_by_name(self, page, name, sort_by):
    limit = 20
    patients = Patient.objects.filter(name=name).order_by(sort_by)
    paginator = Paginator(patients, limit)
    return paginator.page(page).object_list

  
  def _get_patients_by_birthday(self, page, birthday, sort_by):
    limit = 20
    patients = ( Patient.objects.filter(birthday=birthday).order_by(sort_by))
    paginator = Paginator(patients, limit)
    return paginator.page(page).object_list


  def _get_all_patients(self, page, sort_by):
    limit = 20
    patients = Patient.objects.filter().order_by(sort_by)
    paginator = Paginator(patients, limit)
    return paginator.page(page).object_list