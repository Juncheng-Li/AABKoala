from django.contrib.auth.models import User
from django.db.models.functions import datetime
from rest_framework import serializers
from graphs.models import Result, FacilityOutput, TPR, Reading


class UserSerializer(serializers.ModelSerializer):
    result = serializers.HyperlinkedRelatedField(many=True, view_name='result-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'result']


class FacilityOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityOutput
        fields = ['energy_6', 'energy_10', 'energy_15', 'energy_18', 'energy_6FFF', 'energy_10FFF']


class TPRSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPR
        fields = ['energy_6', 'energy_10', 'energy_15', 'energy_18', 'energy_6FFF', 'energy_10FFF']


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ['Reading_101106', 'Reading_110106', 'Reading_205106', 'Reading_208106', 'Reading_205206',
                  'Reading_208206', 'Reading_205306', 'Reading_208306', 'Reading_303106', 'Reading_305106',
                  'Reading_403106', 'Reading_405106', 'Reading_103110', 'Reading_110110', 'Reading_303110',
                  'Reading_305110', 'Reading_403110', 'Reading_405110', 'Reading_103115', 'Reading_110115',
                  'Reading_303115', 'Reading_305115', 'Reading_403115', 'Reading_405115', 'Reading_103118',
                  'Reading_303118', 'Reading_305118', 'Reading_403118', 'Reading_405118', 'Reading_101105',
                  'Reading_110105', 'Reading_303105', 'Reading_305105', 'Reading_103109', 'Reading_110109',
                  'Reading_303109', 'Reading_305109', 'Reading_110118'
                  ]


class ResultSerializer(serializers.ModelSerializer):
    # relative to the user who created it
    user = serializers.ReadOnlyField(source='user.username')
    facilityOutput = FacilityOutputSerializer(many=True)
    TPR = TPRSerializer(many=True)
    Reading = ReadingSerializer(many=True)

    class Meta:
        model = Result
        fields = '__all__'

    def create(self, validated_data):
        facility_outputs_data = validated_data.pop('facilityOutput')
        trps_data = validated_data.pop('TPR')
        Readings_data = validated_data.pop('Reading')

        result = Result.objects.create(**validated_data)
        for facility_output_data in facility_outputs_data:
            FacilityOutput.objects.create(result=result, **facility_output_data)
        for trp_data in trps_data:
            TPR.objects.create(result=result, **trp_data)
        for Readings_data in Readings_data:
            Reading.objects.create(result=result, **Readings_data)
        return result

    def update(self, instance, validated_data):
        facility_outputs_data = validated_data.pop('facilityOutput')
        facilityOutputs = (instance.facilityOutput).all()
        facilityOutputs = list(facilityOutputs)

        trps_data = validated_data.pop('TPR')
        TPRs = (instance.TPR).all()
        TPRs = list(TPRs)

        readings_data = validated_data.pop('Reading')
        Readings = (instance.Reading).all()
        Readings = list(Readings)

        instance.updated = datetime.datetime.now()
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
            facilityOutput.updated = datetime.datetime.now()
            facilityOutput.energy_6 = facility_output_data.get('energy_6', facilityOutput.energy_6)
            facilityOutput.energy_10 = facility_output_data.get('energy_10', facilityOutput.energy_10)
            facilityOutput.energy_18 = facility_output_data.get('energy_18', facilityOutput.energy_18)
            facilityOutput.energy_6FFF = facility_output_data.get('energy_6FFF', facilityOutput.energy_6FFF)
            facilityOutput.energy_10FFF = facility_output_data.get('energy_10FFF', facilityOutput.energy_10FFF)
            facilityOutput.save()

        for trp_data in trps_data:
            TPR = TPRs.pop(0)
            TPR.updated = datetime.datetime.now()
            TPR.energy_6 = trp_data.get('energy_6', TPR.energy_6)
            TPR.energy_10 = trp_data.get('energy_10', TPR.energy_10)
            TPR.energy_18 = trp_data.get('energy_18', TPR.energy_18)
            TPR.energy_6FFF = trp_data.get('energy_6FFF', TPR.energy_6FFF)
            TPR.energy_10FFF = trp_data.get('energy_10FFF', TPR.energy_10FFF)
            TPR.save()

        for reading_data in readings_data:
            Reading = Readings.pop(0)
            Reading.updated = datetime.datetime.now()
            Reading.Reading_101106 = reading_data.get('Reading_101106', Reading.Reading_101106)
            Reading.Reading_110106 = reading_data.get('Reading_110106', Reading.Reading_110106)
            Reading.Reading_205106 = reading_data.get('Reading_205106', Reading.Reading_205106)
            Reading.Reading_208106 = reading_data.get('Reading_208106', Reading.Reading_208106)
            Reading.Reading_205206 = reading_data.get('Reading_205206', Reading.Reading_205206)
            Reading.Reading_208206 = reading_data.get('Reading_208206', Reading.Reading_208206)
            Reading.Reading_205306 = reading_data.get('Reading_205306', Reading.Reading_205306)
            Reading.Reading_208306 = reading_data.get('Reading_208306', Reading.Reading_208306)
            Reading.Reading_303106 = reading_data.get('Reading_303106', Reading.Reading_303106)
            Reading.Reading_305106 = reading_data.get('Reading_305106', Reading.Reading_305106)
            Reading.Reading_403106 = reading_data.get('Reading_403106', Reading.Reading_403106)
            Reading.Reading_405106 = reading_data.get('Reading_405106', Reading.Reading_405106)
            Reading.Reading_103110 = reading_data.get('Reading_103110', Reading.Reading_103110)
            Reading.Reading_110110 = reading_data.get('Reading_110110', Reading.Reading_110110)
            Reading.Reading_303110 = reading_data.get('Reading_303110', Reading.Reading_303110)
            Reading.Reading_305110 = reading_data.get('Reading_305110', Reading.Reading_305110)
            Reading.Reading_403110 = reading_data.get('Reading_403110', Reading.Reading_403110)
            Reading.Reading_405110 = reading_data.get('Reading_405110', Reading.Reading_405110)
            Reading.Reading_103115 = reading_data.get('Reading_103115', Reading.Reading_103115)
            Reading.Reading_110115 = reading_data.get('Reading_110115', Reading.Reading_110115)
            Reading.Reading_303115 = reading_data.get('Reading_303115', Reading.Reading_303115)
            Reading.Reading_305115 = reading_data.get('Reading_305115', Reading.Reading_305115)
            Reading.Reading_403115 = reading_data.get('Reading_403115', Reading.Reading_403115)
            Reading.Reading_405115 = reading_data.get('Reading_405115', Reading.Reading_405115)
            Reading.Reading_103118 = reading_data.get('Reading_103118', Reading.Reading_103118)
            Reading.Reading_303118 = reading_data.get('Reading_303118', Reading.Reading_303118)
            Reading.Reading_305118 = reading_data.get('Reading_305118', Reading.Reading_305118)
            Reading.Reading_403118 = reading_data.get('Reading_403118', Reading.Reading_403118)
            Reading.Reading_405118 = reading_data.get('Reading_405118', Reading.Reading_405118)
            Reading.Reading_101105 = reading_data.get('Reading_101105', Reading.Reading_101105)
            Reading.Reading_110105 = reading_data.get('Reading_110105', Reading.Reading_110105)
            Reading.Reading_303105 = reading_data.get('Reading_303105', Reading.Reading_303105)
            Reading.Reading_305105 = reading_data.get('Reading_305105', Reading.Reading_305105)
            Reading.Reading_103109 = reading_data.get('Reading_103109', Reading.Reading_103109)
            Reading.Reading_110109 = reading_data.get('Reading_110109', Reading.Reading_110109)
            Reading.Reading_303109 = reading_data.get('Reading_303109', Reading.Reading_303109)
            Reading.Reading_305109 = reading_data.get('Reading_305109', Reading.Reading_305109)
            Reading.Reading_110118 = reading_data.get('Reading_110118', Reading.Reading_110118)
            Reading.save()
        return instance
