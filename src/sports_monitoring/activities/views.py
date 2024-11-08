from rest_framework import viewsets
from .models import Activity, ActivityType
from .serializers import ActivitySerializer, ActivityTypeSerializer

class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        activity_type = self.request.query_params.get('activity_type', None)
        
        # Se o parâmetro `activity_type` existir, aplicamos o filtro
        if activity_type:
            queryset = queryset.filter(activity_type__icontains=activity_type)
        return queryset

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    

"""
class ActivityMetricsViewSet(viewsets.ModelViewSet):
    queryset = ActivityMetrics.objects.all()
    serializer_class = ActivityMetricsSerializer

class ActivityHistoryViewSet(viewsets.ModelViewSet):
    queryset = ActivityHistory.objects.all()
    serializer_class = ActivityHistorySerializer
"""
