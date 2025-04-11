from rest_framework import serializers
from .models import ContactMessage, OfficeLocation, InquiryType, HeardFrom, OfficeType

class InquiryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InquiryType
        fields = '__all__'


class HeardFromSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeardFrom
        fields = '__all__'


class OfficeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeType
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    inquiry_type = serializers.PrimaryKeyRelatedField(queryset=InquiryType.objects.all())
    heard_about = serializers.PrimaryKeyRelatedField(queryset=HeardFrom.objects.all())

    class Meta:
        model = ContactMessage
        fields = '__all__'



class OfficeLocationSerializer(serializers.ModelSerializer):
    office_type = serializers.PrimaryKeyRelatedField(queryset=OfficeType.objects.all())

    class Meta:
        model = OfficeLocation
        fields = '__all__'
