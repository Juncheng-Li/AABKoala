import unittest
import requests
from unittest.mock import patch, Mock
from LocalProgram.resultRequest import resultRequest
import json
import http.client
from LocalProgram.config import *
class TestResultRequest(unittest.TestCase):


    def test_insertNewResult(self):
        testRecord = ['{"AuditID": 1111, "RevisionNumber": 1111, "FacilityName": "African Palm Civet", "FacilityID": "FAC-028", "Auditor1": "Velvet", "Auditor2": null, "Auditor3": null, "AuditDate": "2020-09-02", "RepDate": "Q4 2020", "LinacModel": "Korg", "LinacManufacturer": "iX", "PlanningSystemManufacturer": "STA", "tps": "Sun", "Algorithm": "Small", "kqFac": "p", "ACDS": "p", "Phantom": null, "facilityOutput": [{"energy_6": 1.008, "energy_10": null, "energy_15": null, "energy_18": null, "energy_6FFF": null, "energy_10FFF": null}], "TPR": [{"energy_6": null, "energy_10": null, "energy_15": null, "energy_18": null, "energy_6FFF": null, "energy_10FFF": null}], "Reading": [{"Reading_101106": null, "Reading_110106": null, "Reading_205106": null, "Reading_208106": null, "Reading_205206": null, "Reading_208206": null, "Reading_205306": null, "Reading_208306": null, "Reading_303106": null, "Reading_305106": null, "Reading_403106": null, "Reading_405106": null, "Reading_103110": null, "Reading_110110": null, "Reading_303110": null, "Reading_305110": null, "Reading_403110": null, "Reading_405110": null, "Reading_103115": null, "Reading_110115": -0.0065, "Reading_303115": null, "Reading_305115": null, "Reading_403115": null, "Reading_405115": null, "Reading_103118": null, "Reading_110118": null, "Reading_303118": null, "Reading_305118": null, "Reading_403118": null, "Reading_405118": null, "Reading_101105": null, "Reading_110105": null, "Reading_303105": null, "Reading_305105": null, "Reading_103109": null, "Reading_110109": null, "Reading_303109": null, "Reading_305109": null}], "Misdelivery": [{"Misdelivery_101106": 0, "Misdelivery_110106": 0, "Misdelivery_205106": 0, "Misdelivery_208106": 0, "Misdelivery_205206": 0, "Misdelivery_208206": 0, "Misdelivery_205306": 0, "Misdelivery_208306": 0, "Misdelivery_303106": 0, "Misdelivery_305106": 0, "Misdelivery_403106": 0, "Misdelivery_405106": 0, "Misdelivery_103110": 0, "Misdelivery_110110": 0, "Misdelivery_303110": 0, "Misdelivery_305110": 0, "Misdelivery_403110": 0, "Misdelivery_405110": 0, "Misdelivery_103115": 0, "Misdelivery_110115": 0, "Misdelivery_303115": 0, "Misdelivery_305115": 0, "Misdelivery_403115": 0, "Misdelivery_405115": 0, "Misdelivery_103118": 0, "Misdelivery_110118": 0, "Misdelivery_303118": 0, "Misdelivery_305118": 0, "Misdelivery_403118": 0, "Misdelivery_405118": 0, "Misdelivery_101105": 0, "Misdelivery_110105": 0, "Misdelivery_303105": 0, "Misdelivery_305105": 0, "Misdelivery_103109": 0, "Misdelivery_110109": 0, "Misdelivery_303109": 0, "Misdelivery_305109": 0}], "IMRT": [{"c6_p11_6": null, "c6_p12_6": null, "c6_p13_6": null, "c6_p14_6": null, "c6_p15_6": null, "c6_p16_6": null, "c6_p17_6": null, "c7_p11_6": null, "c7_p12_6": null, "c7_p13_6": null, "c7_p14_6": null, "c7_p15_6": null, "c7_p16_6": null, "c7_p17_6": null, "c8_p11_6": null, "c8_p12_6": null, "c8_p13_6": null, "c8_p14_6": null, "c8_p15_6": null, "c8_p17_6": null, "c8_p18_6": null, "c6_p11_10": null, "c6_p12_10": null, "c6_p13_10": null, "c6_p14_10": null, "c6_p15_10": null, "c6_p16_10": null, "c6_p17_10": null, "c7_p11_10": null, "c7_p12_10": null, "c7_p13_10": null, "c7_p14_10": null, "c7_p15_10": null, "c7_p16_10": null, "c7_p17_10": null, "c8_p11_10": null, "c8_p12_10": null, "c8_p13_10": null, "c8_p14_10": null, "c8_p15_10": null, "c8_p17_10": null, "c8_p18_10": null}], "IMRT_misdelivery": [{"c6_p11_6": null, "c6_p12_6": null, "c6_p13_6": null, "c6_p14_6": null, "c6_p15_6": null, "c6_p16_6": null, "c6_p17_6": null, "c7_p11_6": null, "c7_p12_6": null, "c7_p13_6": null, "c7_p14_6": null, "c7_p15_6": null, "c7_p16_6": null, "c7_p17_6": null, "c8_p11_6": null, "c8_p12_6": null, "c8_p13_6": null, "c8_p14_6": null, "c8_p15_6": null, "c8_p17_6": null, "c8_p18_6": null, "c6_p11_10": null, "c6_p12_10": null, "c6_p13_10": null, "c6_p14_10": null, "c6_p15_10": null, "c6_p16_10": null, "c6_p17_10": null, "c7_p11_10": null, "c7_p12_10": null, "c7_p13_10": null, "c7_p14_10": null, "c7_p15_10": null, "c7_p16_10": null, "c7_p17_10": null, "c8_p11_10": null, "c8_p12_10": null, "c8_p13_10": null, "c8_p14_10": null, "c8_p15_10": null, "c8_p17_10": null, "c8_p18_10": null}]}']
        fake_JASON = {'id': 395, 'user': 'root', 'facilityOutput': [
            {'energy_6': '1.0080', 'energy_10': None, 'energy_15': None, 'energy_18': None, 'energy_6FFF': None,
             'energy_10FFF': None}], 'TPR': [
            {'energy_6': None, 'energy_10': None, 'energy_15': None, 'energy_18': None, 'energy_6FFF': None,
             'energy_10FFF': None}], 'Reading': [
            {'Reading_101106': None, 'Reading_110106': None, 'Reading_205106': None, 'Reading_208106': None,
             'Reading_205206': None, 'Reading_208206': None, 'Reading_205306': None, 'Reading_208306': None,
             'Reading_303106': None, 'Reading_305106': None, 'Reading_403106': None, 'Reading_405106': None,
             'Reading_103110': None, 'Reading_110110': None, 'Reading_303110': None, 'Reading_305110': None,
             'Reading_403110': None, 'Reading_405110': None, 'Reading_103115': None, 'Reading_110115': '-0.00650',
             'Reading_303115': None, 'Reading_305115': None, 'Reading_403115': None, 'Reading_405115': None,
             'Reading_103118': None, 'Reading_303118': None, 'Reading_305118': None, 'Reading_403118': None,
             'Reading_405118': None, 'Reading_101105': None, 'Reading_110105': None, 'Reading_303105': None,
             'Reading_305105': None, 'Reading_103109': None, 'Reading_110109': None, 'Reading_303109': None,
             'Reading_305109': None, 'Reading_110118': None}], 'Misdelivery': [
            {'Misdelivery_101106': 0, 'Misdelivery_110106': 0, 'Misdelivery_205106': 0, 'Misdelivery_208106': 0,
             'Misdelivery_205206': 0, 'Misdelivery_208206': 0, 'Misdelivery_205306': 0, 'Misdelivery_208306': 0,
             'Misdelivery_303106': 0, 'Misdelivery_305106': 0, 'Misdelivery_403106': 0, 'Misdelivery_405106': 0,
             'Misdelivery_103110': 0, 'Misdelivery_110110': 0, 'Misdelivery_303110': 0, 'Misdelivery_305110': 0,
             'Misdelivery_403110': 0, 'Misdelivery_405110': 0, 'Misdelivery_103115': 0, 'Misdelivery_110115': 0,
             'Misdelivery_303115': 0, 'Misdelivery_305115': 0, 'Misdelivery_403115': 0, 'Misdelivery_405115': 0,
             'Misdelivery_103118': 0, 'Misdelivery_303118': 0, 'Misdelivery_305118': 0, 'Misdelivery_403118': 0,
             'Misdelivery_405118': 0, 'Misdelivery_101105': 0, 'Misdelivery_110105': 0, 'Misdelivery_303105': 0,
             'Misdelivery_305105': 0, 'Misdelivery_103109': 0, 'Misdelivery_110109': 0, 'Misdelivery_303109': 0,
             'Misdelivery_305109': 0, 'Misdelivery_110118': 0}], 'IMRT': [
            {'c6_p11_6': None, 'c6_p12_6': None, 'c6_p13_6': None, 'c6_p14_6': None, 'c6_p15_6': None, 'c6_p16_6': None,
             'c6_p17_6': None, 'c7_p11_6': None, 'c7_p12_6': None, 'c7_p13_6': None, 'c7_p14_6': None, 'c7_p15_6': None,
             'c7_p16_6': None, 'c7_p17_6': None, 'c8_p11_6': None, 'c8_p12_6': None, 'c8_p13_6': None, 'c8_p14_6': None,
             'c8_p15_6': None, 'c8_p17_6': None, 'c8_p18_6': None, 'c6_p11_10': None, 'c6_p12_10': None,
             'c6_p13_10': None, 'c6_p14_10': None, 'c6_p15_10': None, 'c6_p16_10': None, 'c6_p17_10': None,
             'c7_p11_10': None, 'c7_p12_10': None, 'c7_p13_10': None, 'c7_p14_10': None, 'c7_p15_10': None,
             'c7_p16_10': None, 'c7_p17_10': None, 'c8_p11_10': None, 'c8_p12_10': None, 'c8_p13_10': None,
             'c8_p14_10': None, 'c8_p15_10': None, 'c8_p17_10': None, 'c8_p18_10': None}], 'IMRT_misdelivery': [
            {'c6_p11_6': None, 'c6_p12_6': None, 'c6_p13_6': None, 'c6_p14_6': None, 'c6_p15_6': None, 'c6_p16_6': None,
             'c6_p17_6': None, 'c7_p11_6': None, 'c7_p12_6': None, 'c7_p13_6': None, 'c7_p14_6': None, 'c7_p15_6': None,
             'c7_p16_6': None, 'c7_p17_6': None, 'c8_p11_6': None, 'c8_p12_6': None, 'c8_p13_6': None, 'c8_p14_6': None,
             'c8_p15_6': None, 'c8_p17_6': None, 'c8_p18_6': None, 'c6_p11_10': None, 'c6_p12_10': None,
             'c6_p13_10': None, 'c6_p14_10': None, 'c6_p15_10': None, 'c6_p16_10': None, 'c6_p17_10': None,
             'c7_p11_10': None, 'c7_p12_10': None, 'c7_p13_10': None, 'c7_p14_10': None, 'c7_p15_10': None,
             'c7_p16_10': None, 'c7_p17_10': None, 'c8_p11_10': None, 'c8_p12_10': None, 'c8_p13_10': None,
             'c8_p14_10': None, 'c8_p15_10': None, 'c8_p17_10': None, 'c8_p18_10': None}],
         'created': '2020-10-14T15:51:02.847803Z', 'updated': '2020-10-14T15:51:02.847803Z', 'AuditID': '1111',
         'RevisionNumber': '1111', 'FacilityName': 'African Palm Civet', 'FacilityID': 'FAC-028', 'Auditor1': 'Velvet',
         'Auditor2': None, 'Auditor3': None, 'AuditDate': '2020-09-02', 'RepDate': 'Q4 2020', 'LinacModel': 'Korg',
         'LinacManufacturer': 'iX', 'PlanningSystemManufacturer': 'STA', 'tps': 'Sun', 'Algorithm': 'Small',
         'kqFac': 'p', 'ACDS': 'p', 'Phantom': None}

        # if len(testRecord) == 1:
        #     payload = testRecord[0]
        #     headers = {
        #         'Authorization': self.authorization,
        #         'Content-Type': 'application/json'
        #     }
        #     res = self.conn.request("POST", "/graphs/results/", payload, headers)
        #     with patch(res) as mock_post:
        #         res = self.conn.getresponse()
        #
        #         mock_post.status_code = 200
        #         real_JASON = json.loads(res.decode("utf-8"))

                #assert  fake_JASON == real_JASON
        # testRecord = json.loads(testRecord.decode("utf-8"))
        assert  fake_JASON ==json.loads(testRecord)







