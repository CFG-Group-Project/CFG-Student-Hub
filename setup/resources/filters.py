from .models import *
import django_filters

class MaterialFilter(django_filters.FilterSet):
    class Meta:
        model = Material
        fields = ['week','show','sub_by','program']

class MaterialFilterStudents(django_filters.FilterSet):
    class Meta:
        model = Material
        fields = ['week','program','topics']

