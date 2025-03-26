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

    # Integer filters for price and size
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte", label="Minimum Price")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte", label="Maximum Price")
    min_size = django_filters.NumberFilter(field_name="size", lookup_expr="gte", label="Minimum Size")
    max_size = django_filters.NumberFilter(field_name="size", lookup_expr="lte", label="Maximum Size")

    # Custom range filters from string
    price_range = django_filters.CharFilter(method='filter_price_range')
    size_range = django_filters.CharFilter(method='filter_size_range')

    class Meta:
        model = Property
        fields = [
            "location", "property_type", "build_year",
            "min_price", "max_price", "min_size", "max_size",
            "price_range", "size_range"
        ]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            models.Q(location__icontains=value) | models.Q(property_type__name__icontains=value)
        )

    def filter_price_range(self, queryset, name, value):
        try:
            clean_value = value.replace("$", "").replace(",", "").strip()
            if "+" in clean_value:
                min_val = int(clean_value.replace("+", "").strip())
                return queryset.filter(price__gte=min_val)
            else:
                min_val, max_val = map(int, clean_value.split("-"))
                return queryset.filter(price__gte=min_val, price__lte=max_val)
        except ValueError:
            return queryset

    
    def filter_size_range(self, queryset, name, value):
        try:
            clean_value = value.replace("sqm", "").strip()
            if "+" in clean_value:
                min_val = int(clean_value.replace("+", "").strip())
                return queryset.filter(size__gte=min_val)
            else:
                min_val, max_val = map(int, clean_value.split("-"))
                return queryset.filter(size__gte=min_val, size__lte=max_val)
        except ValueError:
            return queryset
