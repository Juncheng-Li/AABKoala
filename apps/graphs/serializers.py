from rest_framework import serializers
from graphs.models import Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'created', 'updated', 'AuditID', 'RevisionNumber', 'FacilityName', 'FacilityID',
                  'Auditor1', 'Auditor2', 'Auditor3', 'AuditDate', 'RepDate', 'LinacModel', 'LinacManufacturer',
                  'PlanningSystemManufacturer', 'tps', 'Algorithm', 'kqFac', 'ACDS', 'Phantom']
