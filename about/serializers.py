from rest_framework import serializers
from .models import Achievement, Step

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'