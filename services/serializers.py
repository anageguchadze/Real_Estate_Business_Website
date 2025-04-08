from rest_framework import serializers
from .models import SellingService, ManagementService, InvestmentService

class SellingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellingService
        fields = '__all__'

class ManagementServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementService
        fields = '__all__'

class InvestmentServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentService
        fields = '__all__'
