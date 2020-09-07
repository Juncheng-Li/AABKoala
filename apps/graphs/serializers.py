from django.contrib.auth.models import User
from rest_framework import serializers
from graphs.models import Result


class ResultSerializer(serializers.ModelSerializer):
    # relative to the user who created it
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Result
        fields = ['url', 'id', 'created', 'updated', 'AuditID', 'RevisionNumber', 'FacilityName', 'FacilityID',
                  'Auditor1', 'Auditor2', 'Auditor3', 'AuditDate', 'RepDate', 'LinacModel', 'LinacManufacturer',
                  'PlanningSystemManufacturer', 'tps', 'Algorithm', 'kqFac', 'ACDS', 'Phantom', 'user']


class UserSerializer(serializers.ModelSerializer):
    results = serializers.HyperlinkedRelatedField(many=True, view_name='results-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'results']
