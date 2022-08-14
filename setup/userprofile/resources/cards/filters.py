from .models import *
import django_filters


class TopicFilter(django_filters.FilterSet):
    class Meta:
        model = Card
        fields = ['topic']
