import django_filters
from.models import PrivateClasses



class PrivateClassesFilter(django_filters.FilterSet):
    class Meta:
        model=PrivateClasses
        fields='__all__'
        exclude=['coursename','teachername','teacherphonenumber','content']