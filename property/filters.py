import django_filters
from .models import Property
from django.db import models


class PropertyFilter(django_filters.FilterSet):
    # Search bar: Filter by either location OR property type
    search = django_filters.CharFilter(method="filter_search", label="Search Location or Property Type")

    # Dropdown filters
    location = django_filters.CharFilter(field_name="location", lookup_expr="iexact", label="Location")
    property_type = django_filters.CharFilter(field_name="property_type__name", lookup_expr="iexact", label="Property Type")
    build_year = django_filters.NumberFilter(field_name="build_year", lookup_expr="exact", label="Build Year")

    # Min/Max filters for price
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte", label="Minimum Price")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte", label="Maximum Price")

    # Min/Max filters for size
    min_size = django_filters.NumberFilter(field_name="size", lookup_expr="gte", label="Minimum Size")
    max_size = django_filters.NumberFilter(field_name="size", lookup_expr="lte", label="Maximum Size")

    class Meta:
        model = Property
        fields = ["location", "property_type", "build_year", "min_price", "max_price", "min_size", "max_size"]

    def filter_search(self, queryset, name, value):
        """
        Custom filter to search properties by either location or property type.
        """
        return queryset.filter(
            models.Q(location__icontains=value) | models.Q(property_type__name__icontains=value)
        )
