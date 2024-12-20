from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity, ActivityType


class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'
        
class ActivitySerializer(serializers.ModelSerializer):
    # metrics = ActivityMetricsSerializer()
    class Meta:
        model = Activity
        fields = '__all__'

"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ActivityMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityMetrics
        fields = ['distance_km', 'duration_minutes', 'avg_speed_kmh', 'calories_burned', 'elevation_gain']


class ActivityHistorySerializer(serializers.ModelSerializer):
    activity = ActivitySerializer()
    user = UserSerializer()

    class Meta:
        model = ActivityHistory
        fields = ['id', 'user', 'activity', 'created_at']
"""