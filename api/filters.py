from django_filters.rest_framework import FilterSet, NumberFilter, CharFilter
from .models import Event

class EventFilter(FilterSet):
    sport = NumberFilter('competition__sport__id')
    class Meta:
        model = Event
        fields = ['athlete',
        'athlete_age',
        'athlete_team',
        'athlete_NOC',
        'game',
        'sport',
        'competition',
        'medal']
