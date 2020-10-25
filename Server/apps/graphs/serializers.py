from django.contrib.auth.models import User
from django.db.models.functions import datetime
from rest_framework import serializers

from apps.graphs.models import FacilityOutput, TPR, Nds_3dcrt, Nds_3dcrt_misdelivery, Graph, Result, Nds_imrt, \
    Nds_imrt_misdelivery


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


class Nds_3dcrtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nds_3dcrt
        fields = ['code_101106', 'code_110106', 'code_205106', 'code_208106', 'code_205206',
                  'code_208206', 'code_205306', 'code_208306', 'code_303106', 'code_305106',
                  'code_403106', 'code_405106', 'code_103110', 'code_110110', 'code_303110',
                  'code_305110', 'code_403110', 'code_405110', 'code_103115', 'code_110115',
                  'code_303115', 'code_305115', 'code_403115', 'code_405115', 'code_103118',
                  'code_303118', 'code_305118', 'code_403118', 'code_405118', 'code_101105',
                  'code_110105', 'code_303105', 'code_305105', 'code_103109', 'code_110109',
                  'code_303109', 'code_305109', 'code_110118'
                  ]


class Nds_3dcrt_misdeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nds_3dcrt_misdelivery
        fields = ['code_101106', 'code_110106', 'code_205106', 'code_208106', 'code_205206', 'code_208206',
                  'code_205306', 'code_208306', 'code_303106', 'code_305106', 'code_403106', 'code_405106',
                  'code_103110', 'code_110110', 'code_303110', 'code_305110', 'code_403110', 'code_405110',
                  'code_103115', 'code_110115', 'code_303115', 'code_305115', 'code_403115', 'code_405115',
                  'code_103118', 'code_303118', 'code_305118', 'code_403118', 'code_405118', 'code_101105',
                  'code_110105', 'code_303105', 'code_305105', 'code_103109', 'code_110109', 'code_303109',
                  'code_305109', 'code_110118'
                  ]


class Nds_imrtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nds_imrt
        fields = ["code_c6_p11_6", "code_c6_p12_6", "code_c6_p13_6", "code_c6_p14_6", "code_c6_p15_6", "code_c6_p16_6",
                  "code_c6_p17_6", "code_c7_p11_6", "code_c7_p12_6", "code_c7_p13_6", "code_c7_p14_6", "code_c7_p15_6",
                  "code_c7_p16_6", "code_c7_p17_6", "code_c8_p11_6", "code_c8_p12_6", "code_c8_p13_6", "code_c8_p14_6",
                  "code_c8_p15_6", "code_c8_p17_6", "code_c8_p18_6", "code_c6_p11_10", "code_c6_p12_10",
                  "code_c6_p13_10", "code_c6_p14_10", "code_c6_p15_10", "code_c6_p16_10", "code_c6_p17_10",
                  "code_c7_p11_10", "code_c7_p12_10", "code_c7_p13_10", "code_c7_p14_10", "code_c7_p15_10",
                  "code_c7_p16_10", "code_c7_p17_10", "code_c8_p11_10", "code_c8_p12_10", "code_c8_p13_10",
                  "code_c8_p14_10", "code_c8_p15_10", "code_c8_p17_10", "code_c8_p18_10"
                  ]


class Nds_imrt_misdeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nds_imrt_misdelivery
        fields = ["code_c6_p11_6", "code_c6_p12_6", "code_c6_p13_6", "code_c6_p14_6", "code_c6_p15_6", "code_c6_p16_6",
                  "code_c6_p17_6", "code_c7_p11_6",
                  "code_c7_p12_6", "code_c7_p13_6", "code_c7_p14_6", "code_c7_p15_6", "code_c7_p16_6", "code_c7_p17_6",
                  "code_c8_p11_6", "code_c8_p12_6",
                  "code_c8_p13_6", "code_c8_p14_6", "code_c8_p15_6", "code_c8_p17_6", "code_c8_p18_6", "code_c6_p11_10",
                  "code_c6_p12_10", "code_c6_p13_10",
                  "code_c6_p14_10", "code_c6_p15_10", "code_c6_p16_10", "code_c6_p17_10", "code_c7_p11_10",
                  "code_c7_p12_10", "code_c7_p13_10",
                  "code_c7_p14_10", "code_c7_p15_10", "code_c7_p16_10", "code_c7_p17_10", "code_c8_p11_10",
                  "code_c8_p12_10", "code_c8_p13_10",
                  "code_c8_p14_10", "code_c8_p15_10", "code_c8_p17_10", "code_c8_p18_10"
                  ]


class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    # relative to the user who created it
    user = serializers.ReadOnlyField(source='user.username')
    facilityOutput = FacilityOutputSerializer(many=True)
    TPR = TPRSerializer(many=True)
    Nds_3dcrt = Nds_3dcrtSerializer(many=True)
    Nds_3dcrt_misdelivery = Nds_3dcrt_misdeliverySerializer(many=True)
    Nds_imrt = Nds_imrtSerializer(many=True)
    Nds_imrt_misdelivery = Nds_imrt_misdeliverySerializer(many=True)

    class Meta:
        model = Result
        fields = '__all__'

    def create(self, validated_data):
        facility_outputs_data = validated_data.pop('facilityOutput')
        trps_data = validated_data.pop('TPR')
        Nds_3dcrts_data = validated_data.pop('Nds_3dcrt')
        Nds_3dcrt_misdeliveries_data = validated_data.pop('Nds_3dcrt_misdelivery')
        Nds_imrts_data = validated_data.pop('Nds_imrt')
        Nds_imrt_misdeliveries_data = validated_data.pop('Nds_imrt_misdelivery')

        result = Result.objects.create(**validated_data)
        for facility_output_data in facility_outputs_data:
            FacilityOutput.objects.create(result=result, **facility_output_data)
        for trp_data in trps_data:
            TPR.objects.create(result=result, **trp_data)
        for Nds_3dcrt_data in Nds_3dcrts_data:
            Nds_3dcrt.objects.create(result=result, **Nds_3dcrt_data)
        for Nds_3dcrt_misdelivery_data in Nds_3dcrt_misdeliveries_data:
            Nds_3dcrt_misdelivery.objects.create(result=result, **Nds_3dcrt_misdelivery_data)
        for Nds_imrt_data in Nds_imrts_data:
            Nds_imrt.objects.create(result=result, **Nds_imrt_data)
        for Nds_imrt_misdelivery_data in Nds_imrt_misdeliveries_data:
            Nds_imrt_misdelivery.objects.create(result=result, **Nds_imrt_misdelivery_data)
        return result

    def update(self, instance, validated_data):
        facility_outputs_data = validated_data.pop('facilityOutput')
        facilityOutputs = (instance.facilityOutput).all()
        facilityOutputs = list(facilityOutputs)

        trps_data = validated_data.pop('TPR')
        TPRs = (instance.TPR).all()
        TPRs = list(TPRs)

        nds_3dcrts_data = validated_data.pop('Nds_3dcrt')
        Nds_3dcrts = (instance.Nds_3dcrt).all()
        Nds_3dcrts = list(Nds_3dcrts)

        nds_3dcrt_misdeliveryies_data = validated_data.pop('Nds_3dcrt_misdelivery')
        Nds_3dcrt_misdeliveries = (instance.Nds_3dcrt_misdelivery).all()
        Nds_3dcrt_misdeliveries = list(Nds_3dcrt_misdeliveries)

        Nds_imrts_data = validated_data.pop('Nds_imrt')
        Nds_imrts = (instance.Nds_imrt).all()
        Nds_imrts = list(Nds_imrts)

        Nds_imrt_misdeliveries_data = validated_data.pop('Nds_imrt_misdelivery')
        Nds_imrt_misdeliveries = (instance.Nds_imrt_misdelivery).all()
        Nds_imrt_misdeliveries = list(Nds_imrt_misdeliveries)

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

        for nds_3dcrt_data in nds_3dcrts_data:
            Nds_3dcrt = Nds_3dcrts.pop(0)
            Nds_3dcrt.updated = datetime.datetime.now()
            Nds_3dcrt.code_101106 = nds_3dcrt_data.get('code_101106', Nds_3dcrt.code_101106)
            Nds_3dcrt.code_110106 = nds_3dcrt_data.get('code_110106', Nds_3dcrt.code_110106)
            Nds_3dcrt.code_205106 = nds_3dcrt_data.get('code_205106', Nds_3dcrt.code_205106)
            Nds_3dcrt.code_208106 = nds_3dcrt_data.get('code_208106', Nds_3dcrt.code_208106)
            Nds_3dcrt.code_205206 = nds_3dcrt_data.get('code_205206', Nds_3dcrt.code_205206)
            Nds_3dcrt.code_208206 = nds_3dcrt_data.get('code_208206', Nds_3dcrt.code_208206)
            Nds_3dcrt.code_205306 = nds_3dcrt_data.get('code_205306', Nds_3dcrt.code_205306)
            Nds_3dcrt.code_208306 = nds_3dcrt_data.get('code_208306', Nds_3dcrt.code_208306)
            Nds_3dcrt.code_303106 = nds_3dcrt_data.get('code_303106', Nds_3dcrt.code_303106)
            Nds_3dcrt.code_305106 = nds_3dcrt_data.get('code_305106', Nds_3dcrt.code_305106)
            Nds_3dcrt.code_403106 = nds_3dcrt_data.get('code_403106', Nds_3dcrt.code_403106)
            Nds_3dcrt.code_405106 = nds_3dcrt_data.get('code_405106', Nds_3dcrt.code_405106)
            Nds_3dcrt.code_103110 = nds_3dcrt_data.get('code_103110', Nds_3dcrt.code_103110)
            Nds_3dcrt.code_110110 = nds_3dcrt_data.get('code_110110', Nds_3dcrt.code_110110)
            Nds_3dcrt.code_303110 = nds_3dcrt_data.get('code_303110', Nds_3dcrt.code_303110)
            Nds_3dcrt.code_305110 = nds_3dcrt_data.get('code_305110', Nds_3dcrt.code_305110)
            Nds_3dcrt.code_403110 = nds_3dcrt_data.get('code_403110', Nds_3dcrt.code_403110)
            Nds_3dcrt.code_405110 = nds_3dcrt_data.get('code_405110', Nds_3dcrt.code_405110)
            Nds_3dcrt.code_103115 = nds_3dcrt_data.get('code_103115', Nds_3dcrt.code_103115)
            Nds_3dcrt.code_110115 = nds_3dcrt_data.get('code_110115', Nds_3dcrt.code_110115)
            Nds_3dcrt.code_303115 = nds_3dcrt_data.get('code_303115', Nds_3dcrt.code_303115)
            Nds_3dcrt.code_305115 = nds_3dcrt_data.get('code_305115', Nds_3dcrt.code_305115)
            Nds_3dcrt.code_403115 = nds_3dcrt_data.get('code_403115', Nds_3dcrt.code_403115)
            Nds_3dcrt.code_405115 = nds_3dcrt_data.get('code_405115', Nds_3dcrt.code_405115)
            Nds_3dcrt.code_103118 = nds_3dcrt_data.get('code_103118', Nds_3dcrt.code_103118)
            Nds_3dcrt.code_303118 = nds_3dcrt_data.get('code_303118', Nds_3dcrt.code_303118)
            Nds_3dcrt.code_305118 = nds_3dcrt_data.get('code_305118', Nds_3dcrt.code_305118)
            Nds_3dcrt.code_403118 = nds_3dcrt_data.get('code_403118', Nds_3dcrt.code_403118)
            Nds_3dcrt.code_405118 = nds_3dcrt_data.get('code_405118', Nds_3dcrt.code_405118)
            Nds_3dcrt.code_101105 = nds_3dcrt_data.get('code_101105', Nds_3dcrt.code_101105)
            Nds_3dcrt.code_110105 = nds_3dcrt_data.get('code_110105', Nds_3dcrt.code_110105)
            Nds_3dcrt.code_303105 = nds_3dcrt_data.get('code_303105', Nds_3dcrt.code_303105)
            Nds_3dcrt.code_305105 = nds_3dcrt_data.get('code_305105', Nds_3dcrt.code_305105)
            Nds_3dcrt.code_103109 = nds_3dcrt_data.get('code_103109', Nds_3dcrt.code_103109)
            Nds_3dcrt.code_110109 = nds_3dcrt_data.get('code_110109', Nds_3dcrt.code_110109)
            Nds_3dcrt.code_303109 = nds_3dcrt_data.get('code_303109', Nds_3dcrt.code_303109)
            Nds_3dcrt.code_305109 = nds_3dcrt_data.get('code_305109', Nds_3dcrt.code_305109)
            Nds_3dcrt.code_110118 = nds_3dcrt_data.get('code_110118', Nds_3dcrt.code_110118)
            Nds_3dcrt.save()

        for nds_3dcrt_misdelivery_data in nds_3dcrt_misdeliveryies_data:
            Nds_3dcrt_misdelivery = Nds_3dcrt_misdeliveries.pop(0)
            Nds_3dcrt_misdelivery.updated = datetime.datetime.now()
            Nds_3dcrt_misdelivery.code_101106 = nds_3dcrt_misdelivery_data.get('code_101106',
                                                                               Nds_3dcrt_misdelivery.code_101106)
            Nds_3dcrt_misdelivery.code_110106 = nds_3dcrt_misdelivery_data.get('code_110106',
                                                                               Nds_3dcrt_misdelivery.code_110106)
            Nds_3dcrt_misdelivery.code_205106 = nds_3dcrt_misdelivery_data.get('code_205106',
                                                                               Nds_3dcrt_misdelivery.code_205106)
            Nds_3dcrt_misdelivery.code_208106 = nds_3dcrt_misdelivery_data.get('code_208106',
                                                                               Nds_3dcrt_misdelivery.code_208106)
            Nds_3dcrt_misdelivery.code_205206 = nds_3dcrt_misdelivery_data.get('code_205206',
                                                                               Nds_3dcrt_misdelivery.code_205206)
            Nds_3dcrt_misdelivery.code_208206 = nds_3dcrt_misdelivery_data.get('code_208206',
                                                                               Nds_3dcrt_misdelivery.code_208206)
            Nds_3dcrt_misdelivery.code_205306 = nds_3dcrt_misdelivery_data.get('code_205306',
                                                                               Nds_3dcrt_misdelivery.code_205306)
            Nds_3dcrt_misdelivery.code_208306 = nds_3dcrt_misdelivery_data.get('code_208306',
                                                                               Nds_3dcrt_misdelivery.code_208306)
            Nds_3dcrt_misdelivery.code_303106 = nds_3dcrt_misdelivery_data.get('code_303106',
                                                                               Nds_3dcrt_misdelivery.code_303106)
            Nds_3dcrt_misdelivery.code_305106 = nds_3dcrt_misdelivery_data.get('code_305106',
                                                                               Nds_3dcrt_misdelivery.code_305106)
            Nds_3dcrt_misdelivery.code_403106 = nds_3dcrt_misdelivery_data.get('code_403106',
                                                                               Nds_3dcrt_misdelivery.code_403106)
            Nds_3dcrt_misdelivery.code_405106 = nds_3dcrt_misdelivery_data.get('code_405106',
                                                                               Nds_3dcrt_misdelivery.code_405106)
            Nds_3dcrt_misdelivery.code_103110 = nds_3dcrt_misdelivery_data.get('code_103110',
                                                                               Nds_3dcrt_misdelivery.code_103110)
            Nds_3dcrt_misdelivery.code_110110 = nds_3dcrt_misdelivery_data.get('code_110110',
                                                                               Nds_3dcrt_misdelivery.code_110110)
            Nds_3dcrt_misdelivery.code_303110 = nds_3dcrt_misdelivery_data.get('code_303110',
                                                                               Nds_3dcrt_misdelivery.code_303110)
            Nds_3dcrt_misdelivery.code_305110 = nds_3dcrt_misdelivery_data.get('code_305110',
                                                                               Nds_3dcrt_misdelivery.code_305110)
            Nds_3dcrt_misdelivery.code_403110 = nds_3dcrt_misdelivery_data.get('code_403110',
                                                                               Nds_3dcrt_misdelivery.code_403110)
            Nds_3dcrt_misdelivery.code_405110 = nds_3dcrt_misdelivery_data.get('code_405110',
                                                                               Nds_3dcrt_misdelivery.code_405110)
            Nds_3dcrt_misdelivery.code_103115 = nds_3dcrt_misdelivery_data.get('code_103115',
                                                                               Nds_3dcrt_misdelivery.code_103115)
            Nds_3dcrt_misdelivery.code_110115 = nds_3dcrt_misdelivery_data.get('code_110115',
                                                                               Nds_3dcrt_misdelivery.code_110115)
            Nds_3dcrt_misdelivery.code_303115 = nds_3dcrt_misdelivery_data.get('code_303115',
                                                                               Nds_3dcrt_misdelivery.code_303115)
            Nds_3dcrt_misdelivery.code_305115 = nds_3dcrt_misdelivery_data.get('code_305115',
                                                                               Nds_3dcrt_misdelivery.code_305115)
            Nds_3dcrt_misdelivery.code_403115 = nds_3dcrt_misdelivery_data.get('code_403115',
                                                                               Nds_3dcrt_misdelivery.code_403115)
            Nds_3dcrt_misdelivery.code_405115 = nds_3dcrt_misdelivery_data.get('code_405115',
                                                                               Nds_3dcrt_misdelivery.code_405115)
            Nds_3dcrt_misdelivery.code_103118 = nds_3dcrt_misdelivery_data.get('code_103118',
                                                                               Nds_3dcrt_misdelivery.code_103118)
            Nds_3dcrt_misdelivery.code_303118 = nds_3dcrt_misdelivery_data.get('code_303118',
                                                                               Nds_3dcrt_misdelivery.code_303118)
            Nds_3dcrt_misdelivery.code_305118 = nds_3dcrt_misdelivery_data.get('code_305118',
                                                                               Nds_3dcrt_misdelivery.code_305118)
            Nds_3dcrt_misdelivery.code_403118 = nds_3dcrt_misdelivery_data.get('code_403118',
                                                                               Nds_3dcrt_misdelivery.code_403118)
            Nds_3dcrt_misdelivery.code_405118 = nds_3dcrt_misdelivery_data.get('code_405118',
                                                                               Nds_3dcrt_misdelivery.code_405118)
            Nds_3dcrt_misdelivery.code_101105 = nds_3dcrt_misdelivery_data.get('code_101105',
                                                                               Nds_3dcrt_misdelivery.code_101105)
            Nds_3dcrt_misdelivery.code_110105 = nds_3dcrt_misdelivery_data.get('code_110105',
                                                                               Nds_3dcrt_misdelivery.code_110105)
            Nds_3dcrt_misdelivery.code_303105 = nds_3dcrt_misdelivery_data.get('code_303105',
                                                                               Nds_3dcrt_misdelivery.code_303105)
            Nds_3dcrt_misdelivery.code_305105 = nds_3dcrt_misdelivery_data.get('code_305105',
                                                                               Nds_3dcrt_misdelivery.code_305105)
            Nds_3dcrt_misdelivery.code_103109 = nds_3dcrt_misdelivery_data.get('code_103109',
                                                                               Nds_3dcrt_misdelivery.code_103109)
            Nds_3dcrt_misdelivery.code_110109 = nds_3dcrt_misdelivery_data.get('code_110109',
                                                                               Nds_3dcrt_misdelivery.code_110109)
            Nds_3dcrt_misdelivery.code_303109 = nds_3dcrt_misdelivery_data.get('code_303109',
                                                                               Nds_3dcrt_misdelivery.code_303109)
            Nds_3dcrt_misdelivery.code_305109 = nds_3dcrt_misdelivery_data.get('code_305109',
                                                                               Nds_3dcrt_misdelivery.code_305109)
            Nds_3dcrt_misdelivery.code_110118 = nds_3dcrt_misdelivery_data.get('code_110118',
                                                                               Nds_3dcrt_misdelivery.code_110118)
            Nds_3dcrt_misdelivery.save()

        for Nds_imrt_data in Nds_imrts_data:
            Nds_imrt = Nds_imrts.pop(0)
            Nds_imrt.updated = datetime.datetime.now()
            Nds_imrt.code_c6_p11_6 = Nds_imrt_data.get('code_c6_p11_6', Nds_imrt.code_c6_p11_6)
            Nds_imrt.code_c6_p12_6 = Nds_imrt_data.get('code_c6_p12_6', Nds_imrt.code_c6_p12_6)
            Nds_imrt.code_c6_p13_6 = Nds_imrt_data.get('code_c6_p13_6', Nds_imrt.code_c6_p13_6)
            Nds_imrt.code_c6_p14_6 = Nds_imrt_data.get('code_c6_p14_6', Nds_imrt.code_c6_p14_6)
            Nds_imrt.code_c6_p15_6 = Nds_imrt_data.get('code_c6_p15_6', Nds_imrt.code_c6_p15_6)
            Nds_imrt.code_c6_p16_6 = Nds_imrt_data.get('code_c6_p16_6', Nds_imrt.code_c6_p16_6)
            Nds_imrt.code_c6_p17_6 = Nds_imrt_data.get('code_c6_p17_6', Nds_imrt.code_c6_p17_6)
            Nds_imrt.code_c7_p11_6 = Nds_imrt_data.get('code_c7_p11_6', Nds_imrt.code_c7_p11_6)
            Nds_imrt.code_c7_p12_6 = Nds_imrt_data.get('code_c7_p12_6', Nds_imrt.code_c7_p12_6)
            Nds_imrt.code_c7_p13_6 = Nds_imrt_data.get('code_c7_p13_6', Nds_imrt.code_c7_p13_6)
            Nds_imrt.code_c7_p14_6 = Nds_imrt_data.get('code_c7_p14_6', Nds_imrt.code_c7_p14_6)
            Nds_imrt.code_c7_p15_6 = Nds_imrt_data.get('code_c7_p15_6', Nds_imrt.code_c7_p15_6)
            Nds_imrt.code_c7_p16_6 = Nds_imrt_data.get('code_c7_p16_6', Nds_imrt.code_c7_p16_6)
            Nds_imrt.code_c7_p17_6 = Nds_imrt_data.get('code_c7_p17_6', Nds_imrt.code_c7_p17_6)
            Nds_imrt.code_c8_p11_6 = Nds_imrt_data.get('code_c8_p11_6', Nds_imrt.code_c8_p11_6)
            Nds_imrt.code_c8_p12_6 = Nds_imrt_data.get('code_c8_p12_6', Nds_imrt.code_c8_p12_6)
            Nds_imrt.code_c8_p13_6 = Nds_imrt_data.get('code_c8_p13_6', Nds_imrt.code_c8_p13_6)
            Nds_imrt.code_c8_p14_6 = Nds_imrt_data.get('code_c8_p14_6', Nds_imrt.code_c8_p14_6)
            Nds_imrt.code_c8_p15_6 = Nds_imrt_data.get('code_c8_p15_6', Nds_imrt.code_c8_p15_6)
            Nds_imrt.code_c8_p17_6 = Nds_imrt_data.get('code_c8_p17_6', Nds_imrt.code_c8_p17_6)
            Nds_imrt.code_c8_p18_6 = Nds_imrt_data.get('code_c8_p18_6', Nds_imrt.code_c8_p18_6)
            Nds_imrt.code_c6_p11_10 = Nds_imrt_data.get('code_c6_p11_10', Nds_imrt.code_c6_p11_10)
            Nds_imrt.code_c6_p12_10 = Nds_imrt_data.get('code_c6_p12_10', Nds_imrt.code_c6_p12_10)
            Nds_imrt.code_c6_p13_10 = Nds_imrt_data.get('code_c6_p13_10', Nds_imrt.code_c6_p13_10)
            Nds_imrt.code_c6_p14_10 = Nds_imrt_data.get('code_c6_p14_10', Nds_imrt.code_c6_p14_10)
            Nds_imrt.code_c6_p15_10 = Nds_imrt_data.get('code_c6_p15_10', Nds_imrt.code_c6_p15_10)
            Nds_imrt.code_c6_p16_10 = Nds_imrt_data.get('code_c6_p16_10', Nds_imrt.code_c6_p16_10)
            Nds_imrt.code_c6_p17_10 = Nds_imrt_data.get('code_c6_p17_10', Nds_imrt.code_c6_p17_10)
            Nds_imrt.code_c7_p11_10 = Nds_imrt_data.get('code_c7_p11_10', Nds_imrt.code_c7_p11_10)
            Nds_imrt.code_c7_p12_10 = Nds_imrt_data.get('code_c7_p12_10', Nds_imrt.code_c7_p12_10)
            Nds_imrt.code_c7_p13_10 = Nds_imrt_data.get('code_c7_p13_10', Nds_imrt.code_c7_p13_10)
            Nds_imrt.code_c7_p14_10 = Nds_imrt_data.get('code_c7_p14_10', Nds_imrt.code_c7_p14_10)
            Nds_imrt.code_c7_p15_10 = Nds_imrt_data.get('code_c7_p15_10', Nds_imrt.code_c7_p15_10)
            Nds_imrt.code_c7_p16_10 = Nds_imrt_data.get('code_c7_p16_10', Nds_imrt.code_c7_p16_10)
            Nds_imrt.code_c7_p17_10 = Nds_imrt_data.get('code_c7_p17_10', Nds_imrt.code_c7_p17_10)
            Nds_imrt.code_c8_p11_10 = Nds_imrt_data.get('code_c8_p11_10', Nds_imrt.code_c8_p11_10)
            Nds_imrt.code_c8_p12_10 = Nds_imrt_data.get('code_c8_p12_10', Nds_imrt.code_c8_p12_10)
            Nds_imrt.code_c8_p13_10 = Nds_imrt_data.get('code_c8_p13_10', Nds_imrt.code_c8_p13_10)
            Nds_imrt.code_c8_p14_10 = Nds_imrt_data.get('code_c8_p14_10', Nds_imrt.code_c8_p14_10)
            Nds_imrt.code_c8_p15_10 = Nds_imrt_data.get('code_c8_p15_10', Nds_imrt.code_c8_p15_10)
            Nds_imrt.code_c8_p17_10 = Nds_imrt_data.get('code_c8_p17_10', Nds_imrt.code_c8_p17_10)
            Nds_imrt.code_c8_p18_10 = Nds_imrt_data.get('code_c8_p18_10', Nds_imrt.code_c8_p18_10)
            Nds_imrt.save()

        for Nds_imrt_misdelivery_data in Nds_imrt_misdeliveries_data:
            Nds_imrt_misdelivery = Nds_imrt_misdeliveries.pop(0)
            Nds_imrt_misdelivery.updated = datetime.datetime.now()
            Nds_imrt_misdelivery.code_c6_p11_6 = Nds_imrt_misdelivery_data.get('code_c6_p11_6',
                                                                               Nds_imrt_misdelivery.code_c6_p11_6)
            Nds_imrt_misdelivery.code_c6_p12_6 = Nds_imrt_misdelivery_data.get('code_c6_p12_6',
                                                                               Nds_imrt_misdelivery.code_c6_p12_6)
            Nds_imrt_misdelivery.code_c6_p13_6 = Nds_imrt_misdelivery_data.get('code_c6_p13_6',
                                                                               Nds_imrt_misdelivery.code_c6_p13_6)
            Nds_imrt_misdelivery.code_c6_p14_6 = Nds_imrt_misdelivery_data.get('code_c6_p14_6',
                                                                               Nds_imrt_misdelivery.code_c6_p14_6)
            Nds_imrt_misdelivery.code_c6_p15_6 = Nds_imrt_misdelivery_data.get('code_c6_p15_6',
                                                                               Nds_imrt_misdelivery.code_c6_p15_6)
            Nds_imrt_misdelivery.code_c6_p16_6 = Nds_imrt_misdelivery_data.get('code_c6_p16_6',
                                                                               Nds_imrt_misdelivery.code_c6_p16_6)
            Nds_imrt_misdelivery.code_c6_p17_6 = Nds_imrt_misdelivery_data.get('code_c6_p17_6',
                                                                               Nds_imrt_misdelivery.code_c6_p17_6)
            Nds_imrt_misdelivery.code_c7_p11_6 = Nds_imrt_misdelivery_data.get('code_c7_p11_6',
                                                                               Nds_imrt_misdelivery.code_c7_p11_6)
            Nds_imrt_misdelivery.code_c7_p12_6 = Nds_imrt_misdelivery_data.get('code_c7_p12_6',
                                                                               Nds_imrt_misdelivery.code_c7_p12_6)
            Nds_imrt_misdelivery.code_c7_p13_6 = Nds_imrt_misdelivery_data.get('code_c7_p13_6',
                                                                               Nds_imrt_misdelivery.code_c7_p13_6)
            Nds_imrt_misdelivery.code_c7_p14_6 = Nds_imrt_misdelivery_data.get('code_c7_p14_6',
                                                                               Nds_imrt_misdelivery.code_c7_p14_6)
            Nds_imrt_misdelivery.code_c7_p15_6 = Nds_imrt_misdelivery_data.get('code_c7_p15_6',
                                                                               Nds_imrt_misdelivery.code_c7_p15_6)
            Nds_imrt_misdelivery.code_c7_p16_6 = Nds_imrt_misdelivery_data.get('code_c7_p16_6',
                                                                               Nds_imrt_misdelivery.code_c7_p16_6)
            Nds_imrt_misdelivery.code_c7_p17_6 = Nds_imrt_misdelivery_data.get('code_c7_p17_6',
                                                                               Nds_imrt_misdelivery.code_c7_p17_6)
            Nds_imrt_misdelivery.code_c8_p11_6 = Nds_imrt_misdelivery_data.get('code_c8_p11_6',
                                                                               Nds_imrt_misdelivery.code_c8_p11_6)
            Nds_imrt_misdelivery.code_c8_p12_6 = Nds_imrt_misdelivery_data.get('code_c8_p12_6',
                                                                               Nds_imrt_misdelivery.code_c8_p12_6)
            Nds_imrt_misdelivery.code_c8_p13_6 = Nds_imrt_misdelivery_data.get('code_c8_p13_6',
                                                                               Nds_imrt_misdelivery.code_c8_p13_6)
            Nds_imrt_misdelivery.code_c8_p14_6 = Nds_imrt_misdelivery_data.get('code_c8_p14_6',
                                                                               Nds_imrt_misdelivery.code_c8_p14_6)
            Nds_imrt_misdelivery.code_c8_p15_6 = Nds_imrt_misdelivery_data.get('code_c8_p15_6',
                                                                               Nds_imrt_misdelivery.code_c8_p15_6)
            Nds_imrt_misdelivery.code_c8_p17_6 = Nds_imrt_misdelivery_data.get('code_c8_p17_6',
                                                                               Nds_imrt_misdelivery.code_c8_p17_6)
            Nds_imrt_misdelivery.code_c8_p18_6 = Nds_imrt_misdelivery_data.get('code_c8_p18_6',
                                                                               Nds_imrt_misdelivery.code_c8_p18_6)
            Nds_imrt_misdelivery.code_c6_p11_10 = Nds_imrt_misdelivery_data.get('code_c6_p11_10',
                                                                                Nds_imrt_misdelivery.code_c6_p11_10)
            Nds_imrt_misdelivery.code_c6_p12_10 = Nds_imrt_misdelivery_data.get('code_c6_p12_10',
                                                                                Nds_imrt_misdelivery.code_c6_p12_10)
            Nds_imrt_misdelivery.code_c6_p13_10 = Nds_imrt_misdelivery_data.get('code_c6_p13_10',
                                                                                Nds_imrt_misdelivery.code_c6_p13_10)
            Nds_imrt_misdelivery.code_c6_p14_10 = Nds_imrt_misdelivery_data.get('code_c6_p14_10',
                                                                                Nds_imrt_misdelivery.code_c6_p14_10)
            Nds_imrt_misdelivery.code_c6_p15_10 = Nds_imrt_misdelivery_data.get('code_c6_p15_10',
                                                                                Nds_imrt_misdelivery.code_c6_p15_10)
            Nds_imrt_misdelivery.code_c6_p16_10 = Nds_imrt_misdelivery_data.get('code_c6_p16_10',
                                                                                Nds_imrt_misdelivery.code_c6_p16_10)
            Nds_imrt_misdelivery.code_c6_p17_10 = Nds_imrt_misdelivery_data.get('code_c6_p17_10',
                                                                                Nds_imrt_misdelivery.code_c6_p17_10)
            Nds_imrt_misdelivery.code_c7_p11_10 = Nds_imrt_misdelivery_data.get('code_c7_p11_10',
                                                                                Nds_imrt_misdelivery.code_c7_p11_10)
            Nds_imrt_misdelivery.code_c7_p12_10 = Nds_imrt_misdelivery_data.get('code_c7_p12_10',
                                                                                Nds_imrt_misdelivery.code_c7_p12_10)
            Nds_imrt_misdelivery.code_c7_p13_10 = Nds_imrt_misdelivery_data.get('code_c7_p13_10',
                                                                                Nds_imrt_misdelivery.code_c7_p13_10)
            Nds_imrt_misdelivery.code_c7_p14_10 = Nds_imrt_misdelivery_data.get('code_c7_p14_10',
                                                                                Nds_imrt_misdelivery.code_c7_p14_10)
            Nds_imrt_misdelivery.code_c7_p15_10 = Nds_imrt_misdelivery_data.get('code_c7_p15_10',
                                                                                Nds_imrt_misdelivery.code_c7_p15_10)
            Nds_imrt_misdelivery.code_c7_p16_10 = Nds_imrt_misdelivery_data.get('code_c7_p16_10',
                                                                                Nds_imrt_misdelivery.code_c7_p16_10)
            Nds_imrt_misdelivery.code_c7_p17_10 = Nds_imrt_misdelivery_data.get('code_c7_p17_10',
                                                                                Nds_imrt_misdelivery.code_c7_p17_10)
            Nds_imrt_misdelivery.code_c8_p11_10 = Nds_imrt_misdelivery_data.get('code_c8_p11_10',
                                                                                Nds_imrt_misdelivery.code_c8_p11_10)
            Nds_imrt_misdelivery.code_c8_p12_10 = Nds_imrt_misdelivery_data.get('code_c8_p12_10',
                                                                                Nds_imrt_misdelivery.code_c8_p12_10)
            Nds_imrt_misdelivery.code_c8_p13_10 = Nds_imrt_misdelivery_data.get('code_c8_p13_10',
                                                                                Nds_imrt_misdelivery.code_c8_p13_10)
            Nds_imrt_misdelivery.code_c8_p14_10 = Nds_imrt_misdelivery_data.get('code_c8_p14_10',
                                                                                Nds_imrt_misdelivery.code_c8_p14_10)
            Nds_imrt_misdelivery.code_c8_p15_10 = Nds_imrt_misdelivery_data.get('code_c8_p15_10',
                                                                                Nds_imrt_misdelivery.code_c8_p15_10)
            Nds_imrt_misdelivery.code_c8_p17_10 = Nds_imrt_misdelivery_data.get('code_c8_p17_10',
                                                                                Nds_imrt_misdelivery.code_c8_p17_10)
            Nds_imrt_misdelivery.code_c8_p18_10 = Nds_imrt_misdelivery_data.get('code_c8_p18_10',
                                                                                Nds_imrt_misdelivery.code_c8_p18_10)
            Nds_imrt_misdelivery.save()

        return instance
