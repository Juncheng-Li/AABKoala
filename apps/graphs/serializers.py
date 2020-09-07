from django.contrib.auth.models import User
from rest_framework import serializers
from graphs.models import Result, FacilityOutput


class UserSerializer(serializers.ModelSerializer):
    result = serializers.HyperlinkedRelatedField(many=True, view_name='result-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'result']


class FacilityOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityOutput
        fields = ['energy_6', 'energy_10', 'energy_15', 'energy_18', 'energy_6FFF', 'energy_10FFF']


class ResultSerializer(serializers.ModelSerializer):
    # relative to the user who created it
    user = serializers.ReadOnlyField(source='user.username')
    facilityOutput = FacilityOutputSerializer(many=True)

    class Meta:
        model = Result
        fields = '__all__'

    def create(self, validated_data):
        facility_outputs_data = validated_data.pop('facilityOutput')
        result = Result.objects.create(**validated_data)
        for facility_output_data in facility_outputs_data:
            FacilityOutput.objects.create(result=result, **facility_output_data)
        return result

    def update(self, instance, validated_data):
        facility_outputs_data = validated_data.pop('facilityOutput')
        facilityOutputs = (instance.facilityOutput).all()
        facilityOutputs = list(facilityOutputs)

        instance.AuditID = validated_data.get('AuditID', instance.AuditID)
        instance.RevisionNumber = validated_data.get('RevisionNumber', instance.RevisionNumber)
        instance.FacilityName = validated_data.get('FacilityName', instance.FacilityName)
        instance.FacilityID = validated_data.get('FacilityID', instance.FacilityID)
        instance.Auditor1 = validated_data.get('Auditor1', instance.Auditor1)
        instance.Auditor2 = validated_data.get('Auditor2', instance.Auditor2)
        instance.Auditor3 = validated_data.get('Auditor3', instance.Auditor3)
        instance.AuditDate = validated_data.get('AuditDate', instance.AuditDate)
        instance.RepDate = validated_data.get('RepDate', instance.RepDate)
        instance.LinacModel = validated_data.get('LinacModel', instance.LinacModel)
        instance.LinacManufacturer = validated_data.get('LinacManufacturer', instance.LinacManufacturer)
        instance.PlanningSystemManufacturer = validated_data.get('PlanningSystemManufacturer',
                                                                 instance.PlanningSystemManufacturer)
        instance.tps = validated_data.get('tps', instance.tps)
        instance.Algorithm = validated_data.get('Algorithm', instance.Algorithm)
        instance.kqFac = validated_data.get('kqFac', instance.kqFac)
        instance.ACDS = validated_data.get('ACDS', instance.ACDS)
        instance.Phantom = validated_data.get('Phantom', instance.Phantom)
        instance.save()

        for facility_output_data in facility_outputs_data:
            facilityOutput = facilityOutputs.pop(0)
            facilityOutput.energy_6 = facility_output_data.get('energy_6', facilityOutput.energy_6)
            facilityOutput.energy_10 = facility_output_data.get('energy_10', facilityOutput.energy_10)
            facilityOutput.energy_18 = facility_output_data.get('energy_18', facilityOutput.energy_18)
            facilityOutput.energy_6FFF = facility_output_data.get('energy_6FFF', facilityOutput.energy_6FFF)
            facilityOutput.energy_10FFF = facility_output_data.get('energy_10FFF', facilityOutput.energy_10FFF)
            facilityOutput.save()
        return instance
