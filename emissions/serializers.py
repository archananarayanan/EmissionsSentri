from emissions.models import Emissions
from rest_framework import serializers


class EmissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emissions
        fields = ['id', 'date_created', 'accounting_period', 'scope_1', 'scope_2','scope_3']