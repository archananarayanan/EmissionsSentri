from django.shortcuts import render

# Create your views here.
from emissions.models import Emissions
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from emissions.serializers import EmissionsSerializer


class EmissionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows emissions to be viewed
    """
    queryset = Emissions.objects.all().order_by('-date_created')

    def list(self, request):
        serializer = EmissionsSerializer(self.queryset, many=True)
        return Response(serializer.data)
