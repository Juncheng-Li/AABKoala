from django.contrib.auth.models import User
from django.urls import reverse
from requests.auth import HTTPBasicAuth
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, RequestsClient

from apps.graphs.models import Result, Graph
import decimal

from apps.graphs.serializers import ResultSerializer


class AccountTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='root', email='root@gmail', password='root')
        user = User.objects.get(username='root')
        result1 = {
            "id": 1 ,
            "AuditID": "4",
            "RevisionNumber": "5",
            "FacilityName": "Drever",
            "FacilityID": "3",
            "Auditor1": "3",
            "Auditor2": "3",
            "Auditor3": "3",
            "AuditDate": "2016-11-01",
            "RepDate": "3",
            "LinacModel": "3",
            "LinacManufacturer": "3",
            "PlanningSystemManufacturer": "3",
            "tps": "3",
            "Algorithm": "3",
            "kqFac": "3",
            "ACDS": "3",
            "Phantom": "3",
            "facilityOutput": [
                {"energy_6": 1, "energy_10": 1, "energy_15": 1, "energy_18": 1, "energy_6FFF": 1, "energy_10FFF": 1}
            ],
            "TPR": [
                {"energy_6": 1, "energy_10": 1, "energy_15": 1, "energy_18": 1, "energy_6FFF": 1, "energy_10FFF": 1}
            ],
            "Nds_3dcrt": [
                {
                    "code_101106": 0.01, "code_110106": 0.01, "code_205106": 0.01, "code_208106": 0.01,
                    "code_205206": 0.01,
                    "code_208206": 0.01, "code_205306": 0.01, "code_208306": 0.01, "code_303106": 0.01,
                    "code_305106": 0.01,
                    "code_403106": 0.01, "code_405106": 0.01, "code_103110": 0.01, "code_110110": 0.01,
                    "code_303110": 0.01,
                    "code_305110": 0.01, "code_403110": 0.01, "code_405110": 0.01, "code_103115": 0.01,
                    "code_110115": 0.01,
                    "code_303115": 0.01, "code_305115": 0.01, "code_403115": 0.01, "code_405115": 0.01,
                    "code_103118": 0.01,
                    "code_303118": 0.01, "code_305118": 0.01, "code_403118": 0.01, "code_405118": 0.01,
                    "code_101105": 0.01,
                    "code_110105": 0.01, "code_303105": 0.01, "code_305105": 0.01, "code_103109": 0.01,
                    "code_110109": 0.01,
                    "code_303109": 0.01, "code_305109": 0.01, "code_110118": 0.01}
            ],
            "Nds_3dcrt_misdelivery": [
                {
                    "code_101106": 0, "code_110106": 0, "code_205106": 0, "code_208106": 0, "code_205206": 0,
                    "code_208206": 0, "code_205306": 1, "code_208306": 0, "code_303106": 0, "code_305106": 0,
                    "code_403106": 0, "code_405106": 0, "code_103110": 0, "code_110110": 0, "code_303110": 0,
                    "code_305110": 0, "code_403110": 0, "code_405110": 1, "code_103115": 1, "code_110115": 0,
                    "code_303115": 0, "code_305115": 0, "code_403115": 0, "code_405115": 0, "code_103118": 0,
                    "code_303118": 0, "code_305118": 0, "code_403118": 0, "code_405118": 0, "code_101105": 0,
                    "code_110105": 0, "code_303105": 1, "code_305105": 0, "code_103109": 0, "code_110109": 0,
                    "code_303109": 0, "code_305109": 0, "code_110118": 0}
            ],
            "Nds_imrt": [
                {
                    "code_c6_p11_6": 0.026, "code_c6_p12_6": 0.024, "code_c6_p13_6": 0.015, "code_c6_p14_6": -0.01,
                    "code_c6_p15_6": 0.005,
                    "code_c6_p16_6": 0.018, "code_c6_p17_6": 0.024,
                    "code_c7_p11_6": 0.029, "code_c7_p12_6": 0.036, "code_c7_p13_6": 0.033, "code_c7_p14_6": -0.009,
                    "code_c7_p15_6": 0.014,
                    "code_c7_p16_6": 0.017, "code_c7_p17_6": 0.02,
                    "code_c8_p11_6": 0.018, "code_c8_p12_6": 0.021, "code_c8_p13_6": 0.013, "code_c8_p14_6": 0.46,
                    "code_c8_p15_6": 0.019,
                    "code_c8_p17_6": 0.064, "code_c8_p18_6": 0.039,
                    "code_c6_p11_10": None, "code_c6_p12_10": None, "code_c6_p13_10": None, "code_c6_p14_10": None,
                    "code_c6_p15_10": None,
                    "code_c6_p16_10": None, "code_c6_p17_10": None,
                    "code_c7_p11_10": None, "code_c7_p12_10": None, "code_c7_p13_10": None, "code_c7_p14_10": None,
                    "code_c7_p15_10": None,
                    "code_c7_p16_10": None, "code_c7_p17_10": None,
                    "code_c8_p11_10": None, "code_c8_p12_10": None, "code_c8_p13_10": None, "code_c8_p14_10": None,
                    "code_c8_p15_10": None,
                    "code_c8_p17_10": None, "code_c8_p18_10": None
                }
            ],
            "Nds_imrt_misdelivery": [
                {
                    "code_c6_p11_6": 1, "code_c6_p12_6": 0, "code_c6_p13_6": 0, "code_c6_p14_6": 0, "code_c6_p15_6": 0,
                    "code_c6_p16_6": 0, "code_c6_p17_6": 0,
                    "code_c7_p11_6": 0, "code_c7_p12_6": 0, "code_c7_p13_6": 0, "code_c7_p14_6": 0, "code_c7_p15_6": 0,
                    "code_c7_p16_6": 0, "code_c7_p17_6": 0,
                    "code_c8_p11_6": 0, "code_c8_p12_6": 0, "code_c8_p13_6": 0, "code_c8_p14_6": 1, "code_c8_p15_6": 0,
                    "code_c8_p17_6": 0, "code_c8_p18_6": 0,
                    "code_c6_p11_10": 0, "code_c6_p12_10": 0, "code_c6_p13_10": 0, "code_c6_p14_10": 0,
                    "code_c6_p15_10": 0,
                    "code_c6_p16_10": 0, "code_c6_p17_10": 0,
                    "code_c7_p11_10": 0, "code_c7_p12_10": 0, "code_c7_p13_10": 0, "code_c7_p14_10": 1,
                    "code_c7_p15_10": 0,
                    "code_c7_p16_10": 0, "code_c7_p17_10": 0,
                    "code_c8_p11_10": 0, "code_c8_p12_10": 0, "code_c8_p13_10": 0, "code_c8_p14_10": 0,
                    "code_c8_p15_10": 0,
                    "code_c8_p17_10": 0, "code_c8_p18_10": 0
                }
            ]
        }
        serializer = ResultSerializer(data=result1)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

    def test_get_graph(self):
        client = APIClient()
        url = '/graphs/graphManage/'
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_insert_result(self):
        client = APIClient()
        client.login(username='root', password='root')

        url = '/graphs/results/'
        data = {
            "id": 2,
            "AuditID": "4",
            "RevisionNumber": "5",
            "FacilityName": "Drever",
            "FacilityID": "3",
            "Auditor1": "3",
            "Auditor2": "3",
            "Auditor3": "3",
            "AuditDate": "2016-11-01",
            "RepDate": "3",
            "LinacModel": "3",
            "LinacManufacturer": "3",
            "PlanningSystemManufacturer": "3",
            "tps": "3",
            "Algorithm": "3",
            "kqFac": "3",
            "ACDS": "3",
            "Phantom": "3",
            "facilityOutput": [
                {"energy_6": 1, "energy_10": 1, "energy_15": 1, "energy_18": 1, "energy_6FFF": 1, "energy_10FFF": 1}
            ],
            "TPR": [
                {"energy_6": 1, "energy_10": 1, "energy_15": 1, "energy_18": 1, "energy_6FFF": 1, "energy_10FFF": 1}
            ],
            "Nds_3dcrt": [
                {
                    "code_101106": 0.01, "code_110106": 0.01, "code_205106": 0.01, "code_208106": 0.01,
                    "code_205206": 0.01,
                    "code_208206": 0.01, "code_205306": 0.01, "code_208306": 0.01, "code_303106": 0.01,
                    "code_305106": 0.01,
                    "code_403106": 0.01, "code_405106": 0.01, "code_103110": 0.01, "code_110110": 0.01,
                    "code_303110": 0.01,
                    "code_305110": 0.01, "code_403110": 0.01, "code_405110": 0.01, "code_103115": 0.01,
                    "code_110115": 0.01,
                    "code_303115": 0.01, "code_305115": 0.01, "code_403115": 0.01, "code_405115": 0.01,
                    "code_103118": 0.01,
                    "code_303118": 0.01, "code_305118": 0.01, "code_403118": 0.01, "code_405118": 0.01,
                    "code_101105": 0.01,
                    "code_110105": 0.01, "code_303105": 0.01, "code_305105": 0.01, "code_103109": 0.01,
                    "code_110109": 0.01,
                    "code_303109": 0.01, "code_305109": 0.01, "code_110118": 0.01}
            ],
            "Nds_3dcrt_misdelivery": [
                {
                    "code_101106": 0, "code_110106": 0, "code_205106": 0, "code_208106": 0, "code_205206": 0,
                    "code_208206": 0, "code_205306": 1, "code_208306": 0, "code_303106": 0, "code_305106": 0,
                    "code_403106": 0, "code_405106": 0, "code_103110": 0, "code_110110": 0, "code_303110": 0,
                    "code_305110": 0, "code_403110": 0, "code_405110": 1, "code_103115": 1, "code_110115": 0,
                    "code_303115": 0, "code_305115": 0, "code_403115": 0, "code_405115": 0, "code_103118": 0,
                    "code_303118": 0, "code_305118": 0, "code_403118": 0, "code_405118": 0, "code_101105": 0,
                    "code_110105": 0, "code_303105": 1, "code_305105": 0, "code_103109": 0, "code_110109": 0,
                    "code_303109": 0, "code_305109": 0, "code_110118": 0}
            ],
            "Nds_imrt": [
                {
                    "code_c6_p11_6": 0.026, "code_c6_p12_6": 0.024, "code_c6_p13_6": 0.015, "code_c6_p14_6": -0.01,
                    "code_c6_p15_6": 0.005,
                    "code_c6_p16_6": 0.018, "code_c6_p17_6": 0.024,
                    "code_c7_p11_6": 0.029, "code_c7_p12_6": 0.036, "code_c7_p13_6": 0.033, "code_c7_p14_6": -0.009,
                    "code_c7_p15_6": 0.014,
                    "code_c7_p16_6": 0.017, "code_c7_p17_6": 0.02,
                    "code_c8_p11_6": 0.018, "code_c8_p12_6": 0.021, "code_c8_p13_6": 0.013, "code_c8_p14_6": 0.46,
                    "code_c8_p15_6": 0.019,
                    "code_c8_p17_6": 0.064, "code_c8_p18_6": 0.039,
                    "code_c6_p11_10": None, "code_c6_p12_10": None, "code_c6_p13_10": None, "code_c6_p14_10": None,
                    "code_c6_p15_10": None,
                    "code_c6_p16_10": None, "code_c6_p17_10": None,
                    "code_c7_p11_10": None, "code_c7_p12_10": None, "code_c7_p13_10": None, "code_c7_p14_10": None,
                    "code_c7_p15_10": None,
                    "code_c7_p16_10": None, "code_c7_p17_10": None,
                    "code_c8_p11_10": None, "code_c8_p12_10": None, "code_c8_p13_10": None, "code_c8_p14_10": None,
                    "code_c8_p15_10": None,
                    "code_c8_p17_10": None, "code_c8_p18_10": None
                }
            ],
            "Nds_imrt_misdelivery": [
                {
                    "code_c6_p11_6": 1, "code_c6_p12_6": 0, "code_c6_p13_6": 0, "code_c6_p14_6": 0, "code_c6_p15_6": 0,
                    "code_c6_p16_6": 0, "code_c6_p17_6": 0,
                    "code_c7_p11_6": 0, "code_c7_p12_6": 0, "code_c7_p13_6": 0, "code_c7_p14_6": 0, "code_c7_p15_6": 0,
                    "code_c7_p16_6": 0, "code_c7_p17_6": 0,
                    "code_c8_p11_6": 0, "code_c8_p12_6": 0, "code_c8_p13_6": 0, "code_c8_p14_6": 1, "code_c8_p15_6": 0,
                    "code_c8_p17_6": 0, "code_c8_p18_6": 0,
                    "code_c6_p11_10": 0, "code_c6_p12_10": 0, "code_c6_p13_10": 0, "code_c6_p14_10": 0,
                    "code_c6_p15_10": 0,
                    "code_c6_p16_10": 0, "code_c6_p17_10": 0,
                    "code_c7_p11_10": 0, "code_c7_p12_10": 0, "code_c7_p13_10": 0, "code_c7_p14_10": 1,
                    "code_c7_p15_10": 0,
                    "code_c7_p16_10": 0, "code_c7_p17_10": 0,
                    "code_c8_p11_10": 0, "code_c8_p12_10": 0, "code_c8_p13_10": 0, "code_c8_p14_10": 0,
                    "code_c8_p15_10": 0,
                    "code_c8_p17_10": 0, "code_c8_p18_10": 0
                }
            ]
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = Result.objects.get(id=2)
        self.assertEqual(result.FacilityName, 'Drever')
        self.assertEqual(result.Nds_imrt.get().code_c6_p11_6, decimal.Decimal('0.02600'))
