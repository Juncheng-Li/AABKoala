import unittest
import xlrd

import pandas as pd
import math
import numpy as np
import decimal
import re
from LocalProgram.tests.validator import Validator


class getTestingValue:
    xls = pd.read_excel(r'C:\Users\mmwan\Desktop\SD\LocalProgram\upload\uploadingData.xlsx')
    # print(xls)
    for col in xls.columns:
        auditIdValue = map(str, xls['AuditID'].tolist())
        revisionNumberValue = map(str, xls['RevisionNumber'].tolist())
        facilityNameValue = map(str, xls['FacilityName'].tolist())
        facilityIDValue = map(str, xls['FacilityID'].tolist())
        auditor1Value = map(str, xls['Auditor1'].tolist())
        auditDateValue = map(str, xls['AuditDate'].tolist())
        repDateValue = map(str, xls['RepDate'].tolist())
        linacModelValue = map(str, xls['LinacModel'].tolist())
        linacManufacturerValue = map(str, xls['LinacManufacturer'].tolist())
        planningSystemManufacturerValue = map(str, xls['PlanningSystemManufacturer'].tolist())
        tpsValue = map(str, xls['LinacManufacturer'].tolist())
        algorithmValue = map(str, xls['tps'].tolist())
        kqFacValue = map(str, xls['kqFac'].tolist())
        ACDSValue = map(str, xls['ACDS'].tolist())
        phantomValue = map(str, xls['Phantom'].tolist())
        fac_6 = map(str, xls['fac_6'].tolist())
        fac_10 = map(str, xls['fac_10'].tolist())
        fac_15 = map(str, xls['fac_15'].tolist())
        fac_18 = map(str, xls['fac_18'].tolist())
        fac_6FFF = map(str, xls['fac_6FFF'].tolist())
        fac_10FFF = map(str, xls['fac_10FFF'].tolist())
        TPR_6 = map(str, xls['TPR_6'].tolist())
        TPR_10 = map(str, xls['TPR_10'].tolist())
        TPR_15 = map(str, xls['TPR_15'].tolist())
        TPR_18 = map(str, xls['TPR_18'].tolist())
        TPR_6FFF = map(str, xls['TPR_6FFF'].tolist())
        TPR_10FFF = map(str, xls['TPR_10FFF'].tolist())
        Reading_101106 = map(str, xls['Reading_101106'].tolist())
        Reading_205106 = map(str, xls['Reading_205106'].tolist())
        Reading_208106 = map(str, xls['Reading_208106'].tolist())
        Reading_205206 = map(str, xls['Reading_205206'].tolist())
        Reading_208206 = map(str, xls['Reading_208206'].tolist())
        Reading_205306 = map(str, xls['Reading_205306'].tolist())
        Reading_208306 = map(str, xls['Reading_208306'].tolist())
        Reading_303106 = map(str, xls['Reading_303106'].tolist())
        Reading_305106 = map(str, xls['Reading_305106'].tolist())
        Reading_403106 = map(str, xls['Reading_403106'].tolist())
        Reading_405106 = map(str, xls['Reading_405106'].tolist())
        Reading_103110 = map(str, xls['Reading_103110'].tolist())
        Reading_110110 = map(str, xls['Reading_110110'].tolist())
        Reading_303110 = map(str, xls['Reading_303110'].tolist())
        Reading_305110 = map(str, xls['Reading_305110'].tolist())
        Reading_403110 = map(str, xls['Reading_403110'].tolist())
        Reading_405110 = map(str, xls['Reading_405110'].tolist())
        Reading_103115 = map(str, xls['Reading_103115'].tolist())
        Reading_110115 = map(str, xls['Reading_110115'].tolist())
        Reading_303115 = map(str, xls['Reading_303115'].tolist())
        Reading_305115 = map(str, xls['Reading_305115'].tolist())
        Reading_403115 = map(str, xls['Reading_403115'].tolist())
        Reading_405115 = map(str, xls['Reading_405115'].tolist())
        Reading_103118 = map(str, xls['Reading_103118'].tolist())
        Reading_110118 = map(str, xls['Reading_110118'].tolist())
        Reading_303118 = map(str, xls['Reading_303118'].tolist())
        Reading_305118 = map(str, xls['Reading_305118'].tolist())
        Reading_403118 = map(str, xls['Reading_403118'].tolist())
        Reading_405118 = map(str, xls['Reading_405118'].tolist())
        Reading_101105 = map(str, xls['Reading_101105'].tolist())
        Reading_110105 = map(str, xls['Reading_110105'].tolist())
        Reading_303105 = map(str, xls['Reading_303105'].tolist())
        Reading_305105 = map(str, xls['Reading_305105'].tolist())
        Reading_103109 = map(str, xls['Reading_103109'].tolist())
        Reading_110109 = map(str, xls['Reading_110109'].tolist())
        Reading_303109 = map(str, xls['Reading_303109'].tolist())
        Reading_305109 = map(str, xls['Reading_305109'].tolist())
        Misdelivery_101106 = map(str, xls['Misdelivery_101106'].tolist())
        Misdelivery_110106 = map(str, xls['Misdelivery_110106'].tolist())
        Misdelivery_205106 = map(str, xls['Misdelivery_205106'].tolist())
        Misdelivery_208106 = map(str, xls['Misdelivery_208106'].tolist())
        Misdelivery_205206 = map(str, xls['Misdelivery_205206'].tolist())
        Misdelivery_208206 = map(str, xls['Misdelivery_208206'].tolist())
        Misdelivery_205306 = map(str, xls['Misdelivery_205306'].tolist())
        Misdelivery_208306 = map(str, xls['Misdelivery_208306'].tolist())
        Misdelivery_303106 = map(str, xls['Misdelivery_303106'].tolist())
        Misdelivery_305106 = map(str, xls['Misdelivery_305106'].tolist())
        Misdelivery_403106 = map(str, xls['Misdelivery_403106'].tolist())
        Misdelivery_405106 = map(str, xls['Misdelivery_405106'].tolist())
        Misdelivery_103110 = map(str, xls['Misdelivery_103110'].tolist())
        Misdelivery_110110 = map(str, xls['Misdelivery_110110'].tolist())
        Misdelivery_303110 = map(str, xls['Misdelivery_303110'].tolist())
        Misdelivery_305110 = map(str, xls['Misdelivery_305110'].tolist())
        Misdelivery_403110 = map(str, xls['Misdelivery_403110'].tolist())
        Misdelivery_405110 = map(str, xls['Misdelivery_405110'].tolist())
        Misdelivery_103115 = map(str, xls['Misdelivery_103115'].tolist())
        Misdelivery_110115 = map(str, xls['Misdelivery_110115'].tolist())
        Misdelivery_303115 = map(str, xls['Misdelivery_303115'].tolist())
        Misdelivery_305115 = map(str, xls['Misdelivery_305115'].tolist())
        Misdelivery_403115 = map(str, xls['Misdelivery_403115'].tolist())
        Misdelivery_405115 = map(str, xls['Misdelivery_405115'].tolist())
        Misdelivery_103118 = map(str, xls['Misdelivery_103118'].tolist())
        Misdelivery_110118 = map(str, xls['Misdelivery_110118'].tolist())
        Misdelivery_303118 = map(str, xls['Misdelivery_303118'].tolist())
        Misdelivery_305118 = map(str, xls['Misdelivery_305118'].tolist())
        Misdelivery_403118 = map(str, xls['Misdelivery_403118'].tolist())
        Misdelivery_405118 = map(str, xls['Misdelivery_405118'].tolist())
        Misdelivery_101105 = map(str, xls['Misdelivery_101105'].tolist())
        Misdelivery_110105 = map(str, xls['Misdelivery_110105'].tolist())
        Misdelivery_303105 = map(str, xls['Misdelivery_303105'].tolist())
        Misdelivery_305105 = map(str, xls['Misdelivery_305105'].tolist())
        Misdelivery_103109 = map(str, xls['Misdelivery_103109'].tolist())
        Misdelivery_110109 = map(str, xls['Misdelivery_110109'].tolist())
        Misdelivery_303109 = map(str, xls['Misdelivery_303109'].tolist())
        Misdelivery_305109 = map(str, xls['Misdelivery_305109'].tolist())
        c6_p11_6 = map(str, xls['c6_p11_6'].tolist())
        c6_p12_6 = map(str, xls['c6_p12_6'].tolist())
        c6_p13_6 = map(str, xls['c6_p13_6'].tolist())
        c6_p14_6 = map(str, xls['c6_p14_6'].tolist())
        c6_p15_6 = map(str, xls['c6_p15_6'].tolist())
        c6_p16_6 = map(str, xls['c6_p16_6'].tolist())
        c6_p17_6 = map(str, xls['c6_p17_6'].tolist())
        c7_p11_6 = map(str, xls['c7_p11_6'].tolist())
        c7_p12_6 = map(str, xls['c7_p12_6'].tolist())
        c7_p13_6 = map(str, xls['c7_p13_6'].tolist())
        c7_p14_6 = map(str, xls['c7_p14_6'].tolist())
        c7_p15_6 = map(str, xls['c7_p15_6'].tolist())
        c7_p16_6 = map(str, xls['c7_p16_6'].tolist())
        c7_p17_6 = map(str, xls['c7_p17_6'].tolist())
        c8_p11_6 = map(str, xls['c8_p11_6'].tolist())
        c8_p12_6 = map(str, xls['c8_p12_6'].tolist())
        c8_p13_6 = map(str, xls['c8_p13_6'].tolist())
        c8_p14_6 = map(str, xls['c8_p14_6'].tolist())
        c8_p15_6 = map(str, xls['c8_p15_6'].tolist())
        c8_p17_6 = map(str, xls['c8_p17_6'].tolist())
        c8_p18_6 = map(str, xls['c8_p18_6'].tolist())
        c6_p11_10 = map(str, xls['c6_p11_10'].tolist())
        c6_p12_10 = map(str, xls['c6_p12_10'].tolist())
        c6_p13_10 = map(str, xls['c6_p13_10'].tolist())
        c6_p14_10 = map(str, xls['c6_p14_10'].tolist())
        c6_p15_10 = map(str, xls['c6_p15_10'].tolist())
        c6_p16_10 = map(str, xls['c6_p16_10'].tolist())
        c6_p17_10 = map(str, xls['c6_p17_10'].tolist())
        c7_p11_10 = map(str, xls['c7_p11_10'].tolist())
        c7_p12_10 = map(str, xls['c7_p12_10'].tolist())
        c7_p13_10 = map(str, xls['c7_p13_10'].tolist())
        c7_p14_10 = map(str, xls['c7_p14_10'].tolist())
        c7_p15_10 = map(str, xls['c7_p15_10'].tolist())
        c7_p16_10 = map(str, xls['c7_p16_10'].tolist())
        c7_p17_10 = map(str, xls['c7_p17_10'].tolist())
        c8_p11_10 = map(str, xls['c8_p11_10'].tolist())
        c8_p12_10 = map(str, xls['c8_p12_10'].tolist())
        c8_p13_10 = map(str, xls['c8_p13_10'].tolist())
        c8_p14_10 = map(str, xls['c8_p14_10'].tolist())
        c8_p15_10 = map(str, xls['c8_p15_10'].tolist())
        c8_p17_10 = map(str, xls['c8_p17_10'].tolist())
        c8_p18_10 = map(str, xls['c8_p18_10'].tolist())
        imrt_misdelivery_c6_p11_6 = map(str, xls['imrt_misdelivery_c6_p11_6'].tolist())
        imrt_misdelivery_c6_p12_6 = map(str, xls['imrt_misdelivery_c6_p12_6'].tolist())
        imrt_misdelivery_c6_p13_6 = map(str, xls['imrt_misdelivery_c6_p13_6'].tolist())
        imrt_misdelivery_c6_p14_6 = map(str, xls['imrt_misdelivery_c6_p14_6'].tolist())
        imrt_misdelivery_c6_p15_6 = map(str, xls['imrt_misdelivery_c6_p15_6'].tolist())
        imrt_misdelivery_c6_p16_6 = map(str, xls['imrt_misdelivery_c6_p16_6'].tolist())
        imrt_misdelivery_c6_p17_6 = map(str, xls['imrt_misdelivery_c6_p17_6'].tolist())
        imrt_misdelivery_c7_p11_6 = map(str, xls['imrt_misdelivery_c7_p11_6'].tolist())
        imrt_misdelivery_c7_p12_6 = map(str, xls['imrt_misdelivery_c7_p12_6'].tolist())
        imrt_misdelivery_c7_p13_6 = map(str, xls['imrt_misdelivery_c7_p13_6'].tolist())
        imrt_misdelivery_c7_p14_6 = map(str, xls['imrt_misdelivery_c7_p14_6'].tolist())
        imrt_misdelivery_c7_p15_6 = map(str, xls['imrt_misdelivery_c7_p15_6'].tolist())
        imrt_misdelivery_c7_p16_6 = map(str, xls['imrt_misdelivery_c7_p16_6'].tolist())
        imrt_misdelivery_c7_p17_6 = map(str, xls['imrt_misdelivery_c7_p17_6'].tolist())
        imrt_misdelivery_c8_p11_6 = map(str, xls['imrt_misdelivery_c8_p11_6'].tolist())
        imrt_misdelivery_c8_p12_6 = map(str, xls['imrt_misdelivery_c8_p12_6'].tolist())
        imrt_misdelivery_c8_p13_6 = map(str, xls['imrt_misdelivery_c8_p13_6'].tolist())
        imrt_misdelivery_c8_p14_6 = map(str, xls['imrt_misdelivery_c8_p14_6'].tolist())
        imrt_misdelivery_c8_p15_6 = map(str, xls['imrt_misdelivery_c8_p15_6'].tolist())
        imrt_misdelivery_c8_p17_6 = map(str, xls['imrt_misdelivery_c8_p17_6'].tolist())
        imrt_misdelivery_c8_p18_6 = map(str, xls['imrt_misdelivery_c8_p18_6'].tolist())
        imrt_misdelivery_c6_p11_10 = map(str, xls['imrt_misdelivery_c6_p11_10'].tolist())
        imrt_misdelivery_c6_p12_10 = map(str, xls['imrt_misdelivery_c6_p12_10'].tolist())
        imrt_misdelivery_c6_p13_10 = map(str, xls['imrt_misdelivery_c6_p13_10'].tolist())
        imrt_misdelivery_c6_p14_10 = map(str, xls['imrt_misdelivery_c6_p14_10'].tolist())
        imrt_misdelivery_c6_p15_10 = map(str, xls['imrt_misdelivery_c6_p15_10'].tolist())
        imrt_misdelivery_c6_p16_10 = map(str, xls['imrt_misdelivery_c6_p16_10'].tolist())
        imrt_misdelivery_c6_p17_10 = map(str, xls['imrt_misdelivery_c6_p17_10'].tolist())
        imrt_misdelivery_c7_p11_10 = map(str, xls['imrt_misdelivery_c7_p11_10'].tolist())
        imrt_misdelivery_c7_p12_10 = map(str, xls['imrt_misdelivery_c7_p12_10'].tolist())
        imrt_misdelivery_c7_p13_10 = map(str, xls['imrt_misdelivery_c7_p13_10'].tolist())
        imrt_misdelivery_c7_p14_10 = map(str, xls['imrt_misdelivery_c7_p14_10'].tolist())
        imrt_misdelivery_c7_p15_10 = map(str, xls['imrt_misdelivery_c7_p15_10'].tolist())
        imrt_misdelivery_c7_p16_10 = map(str, xls['imrt_misdelivery_c7_p16_10'].tolist())
        imrt_misdelivery_c7_p17_10 = map(str, xls['imrt_misdelivery_c7_p17_10'].tolist())
        imrt_misdelivery_c8_p11_10 = map(str, xls['imrt_misdelivery_c8_p11_10'].tolist())
        imrt_misdelivery_c8_p12_10 = map(str, xls['imrt_misdelivery_c8_p12_10'].tolist())
        imrt_misdelivery_c8_p13_10 = map(str, xls['imrt_misdelivery_c8_p13_10'].tolist())
        imrt_misdelivery_c8_p14_10 = map(str, xls['imrt_misdelivery_c8_p14_10'].tolist())
        imrt_misdelivery_c8_p15_10 = map(str, xls['imrt_misdelivery_c8_p15_10'].tolist())
        imrt_misdelivery_c8_p17_10 = map(str, xls['imrt_misdelivery_c8_p17_10'].tolist())
        imrt_misdelivery_c8_p18_10 = map(str, xls['imrt_misdelivery_c8_p18_10'].tolist())


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_it_will_accept_a_valid_revisionNumber(self):
        try:
            revisionNumber =getTestingValue.revisionNumberValue
            print(revisionNumber)
            for eachRevisionNumber in revisionNumber:
                print(eachRevisionNumber)
                result = self.validator.check_revisionNumber_is_valid(eachRevisionNumber)
                self.assertTrue(result)
        except AssertionError:
            print(eachRevisionNumber + ' is not valid revisionNumber . '
                                       '\nPlease check: '
                                       '2. No space between revisionNumber. '
                                       '3. revisionNumber can be Null. '
                  )
            # print('AuditID is not valid')

    def test_it_will_accept_a_valid_auditID(self):
        try:
            # Assume
            auditID = getTestingValue.auditIdValue
            for eachAuditID in auditID:
                #print(eachAuditID)
                # Action
                result = self.validator.check_auditID_is_valid(eachAuditID)
                # Assert
                self.assertTrue(result)
        except AssertionError:
            print(eachAuditID + ' is not valid AuditID . ')
            print('Please check: 1. AuditID should have 4 digit. 2. No space between AuditID. 3. AuditID can not be '
                  'Null. ')

    def test_it_will_accept_a_valid_FacilityName(self):
        try:
            facilityName = getTestingValue.facilityNameValue
            for eachFacilityName in facilityName:
                print(eachFacilityName)
                result = self.validator.check_facilityNameValue_is_valid(eachFacilityName)
                self.assertTrue(result)
        except AssertionError:
            print(eachFacilityName + ' is not valid FacilityName '
                                     '\nPlease check: '
                                     '1. FacilityName can not be Null. '
                                     '2. FacilityName should greater then 4 char. '
                  )

    def test_it_will_accept_a_valid_Auditor1(self):
        try:
            auditor1 = getTestingValue.auditor1Value
            for eachAuditor1 in auditor1:
                result = self.validator.check_auditor1_is_valid(eachAuditor1)
                self.assertTrue(result)
        except AssertionError:
            print(eachAuditor1 + ' is not valid Auditor1 '
                                 '\nPlease check: '
                                 '1. Auditor1 can not be Null. '
                  )

    def test_it_will_accept_a_valid_AuditDateValue(self):
        try:
            auditDate = getTestingValue.auditDateValue

            for eachAuditDate in auditDate:
                # print(eachAuditor1)
                result = self.validator.check_auditDate_is_valid(eachAuditDate)
                self.assertTrue(result)
        except AssertionError:
            print(eachAuditDate + ' is not valid AuditDate '
                                  '\nPlease check: '
                                  '1. Auditor1 can not be Null. '
                  )

    # RepDate can be null. Contains number and character

    def test_it_will_accept_a_valid_linacModel(self):
        try:
            linacModel = getTestingValue.linacModelValue
            for eachLinacModel in linacModel:
                print(eachLinacModel)
                result = self.validator.check_linacModel_is_valid(eachLinacModel)
                self.assertTrue(result)
        except AssertionError:
            print(eachLinacModel + ' is not valid LinacModel '
                                   '\nPlease check: '
                                   '1. LinacModel can not be Null. '
                  )

    def test_it_will_accept_a_valid_linacManufacturer(self):
        try:
            linacManufacturer = getTestingValue.linacManufacturerValue
            for eachLinacManufacturer in linacManufacturer:
                print(eachLinacManufacturer)
                result = self.validator.check_linacManufacturer_is_valid(eachLinacManufacturer)
                self.assertTrue(result)
        except AssertionError:
            print(eachLinacManufacturer + ' is not valid LinacManufacturer  '
                                          '\nPlease check: '
                                          '1. LinacManufacturer can not be Null. '
                  )

    def test_it_will_accept_a_valid_planningSystemManufacturer(self):
        try:
            planningSystemManufacturer = getTestingValue.linacManufacturerValue
            for eachPlanningSystemManufacturer in planningSystemManufacturer:
                # print(eachPlanningSystemManufacturer)
                result = self.validator.check_repDate_is_valid(eachPlanningSystemManufacturer)
                self.assertTrue(result)
        except AssertionError:
            print(eachPlanningSystemManufacturer + ' is not valid PlanningSystemManufacturer  '
                                                   '\nPlease check: '
                                                   '1. LinacManufacturer can not be Null. '
                  )

    # tps can be null.

    def test_it_will_accept_a_valid_algorithm(self):
        try:
            algorithm = getTestingValue.algorithmValue
            for eachAlgorithm in algorithm:
                # print(eachPlanningSystemManufacturer)
                result = self.validator.check_planningSystemManufacturer_is_valid(eachAlgorithm)
                self.assertTrue(result)

        except AssertionError:
            print(eachAlgorithm + ' is not valid algorithm  '
                                  '\nPlease check: '
                                  '1. algorithm can not be Null. '
                  )

    def test_it_will_accept_a_valid_ACDS(self):
        try:
            ACDS = getTestingValue.ACDSValue
            for eachACDS in ACDS:
                # print(eachPlanningSystemManufacturer)
                result = self.validator.check_planningSystemManufacturer_is_valid(eachACDS)
                self.assertTrue(result)

        except AssertionError:
            print(eachACDS + ' is not valid ACDS'
                             '\nPlease check: '
                             '1. ACDS can not be Null. '
                  )

    def test_it_will_accept_a_valid_fac(self):
        fac_6 = getTestingValue.fac_6
        fac_10 = getTestingValue.fac_10
        fac_15 = getTestingValue.fac_15
        fac_18 = getTestingValue.fac_18
        fac_6FFF = getTestingValue.fac_6FFF
        fac_10FFF = getTestingValue.fac_10FFF

        try:
            facs = []
            for fac_6 in fac_6:
                facs.append(fac_6)

            for fac_10 in fac_10:
                facs.append(fac_10)

            for fac_15 in fac_15:
                facs.append(fac_15)

            for fac_18 in fac_18:
                facs.append(fac_18)

            for fac_6FFF in fac_6FFF:
                facs.append(fac_6FFF)

            for fac_10FFF in fac_10FFF:
                facs.append(fac_10FFF)

            for facsValue in facs:
                result = self.validator.check_facsValue_is_valid(facsValue)
                self.assertTrue(result)

        except AssertionError:
            print(facsValue + ' is not valid facsValue'
                             '\nPlease check: '
                             '1. facsValue only contain number. '
                  )

    '''
    def test_it_will_accept_a_valid_fac(self):
        Reading_101106= getTestingValue.Reading_101106
        Reading_110106= getTestingValue.Reading_110106
        Reading_205206= getTestingValue.Reading_205206
        Reading_208206= getTestingValue.Reading_208206
        Reading_205306= getTestingValue.Reading_205306
        Reading_208306= getTestingValue.Reading_208306
        Reading_303106= getTestingValue.Reading_303106
        Reading_305106= getTestingValue.Reading_305106
        Reading_403106= getTestingValue.Reading_403106
        Reading_405106= getTestingValue.Reading_405106
        Reading_103110= getTestingValue.Reading_101106
        Reading_110110= getTestingValue.Reading_103110
        Reading_303110= getTestingValue.Reading_101106
        Reading_305110= getTestingValue.Reading_303110
        Reading_403110= getTestingValue.Reading_403110
        Reading_405110= getTestingValue.Reading_405110
        Reading_103115= getTestingValue.Reading_103115
        Reading_110115= getTestingValue.Reading_110115
        Reading_303115= getTestingValue.Reading_303115
        Reading_305115= getTestingValue.Reading_305115
        Reading_403115= getTestingValue.Reading_403115
        Reading_405115= getTestingValue.Reading_405115
        Reading_103118= getTestingValue.Reading_103118
        Reading_110118= getTestingValue.Reading_110118
        Reading_303118= getTestingValue.Reading_303118
        Reading_305118= getTestingValue.Reading_305118
        Reading_403118= getTestingValue.Reading_403118
        Reading_405118= getTestingValue.Reading_405118
        Reading_101105= getTestingValue.Reading_101105
        Reading_110105= getTestingValue.Reading_110105
        Reading_303105= getTestingValue.Reading_303105
        Reading_305105= getTestingValue.Reading_305105
        Reading_103109= getTestingValue.Reading_103109
        Reading_110109= getTestingValue.Reading_110109
        Reading_303109= getTestingValue.Reading_303109
        Reading_305109= getTestingValue.Reading_305109

        facs = []
        for Reading_101106 in Reading_101106:
            facs.append(Reading_101106)
        
        for Reading_110106 in Reading_110106:
            facs.append(Reading_110106)
        
        for Reading_205206 in Reading_205206:
            facs.append(Reading_110106)
        
        for Reading_205306 in Reading_205306:
            facs.append(Reading_101106)
        
        for Reading_101106 in Reading_101106:
            facs.append(Reading_101106)
        

        Misdelivery_101106= getTestingValue.Misdelivery_101106
        Misdelivery_110106= getTestingValue.Misdelivery_110106
        Misdelivery_205106= getTestingValue.Reading_101106
        Misdelivery_208106= getTestingValue.Reading_101106
        Misdelivery_205206= getTestingValue.Reading_101106
        Misdelivery_208206= getTestingValue.Reading_101106
        Misdelivery_205306= getTestingValue.Reading_101106
        Misdelivery_208306= getTestingValue.Reading_101106
        Misdelivery_303106= getTestingValue.Reading_101106
        Misdelivery_305106= getTestingValue.Reading_101106
        Misdelivery_403106= getTestingValue.Reading_101106
        Misdelivery_405106= getTestingValue.Reading_101106
        Misdelivery_103110= getTestingValue.Reading_101106
        Misdelivery_110110= getTestingValue.Reading_101106
        Misdelivery_303110= getTestingValue.Reading_101106
        Misdelivery_305110= getTestingValue.Reading_101106
        Misdelivery_403110= getTestingValue.Reading_101106
        Misdelivery_405110= getTestingValue.Reading_101106
        Misdelivery_103115= getTestingValue.Reading_101106
        Misdelivery_110115= getTestingValue.Reading_101106
        Misdelivery_303115= getTestingValue.Reading_101106
        Misdelivery_305115= getTestingValue.Reading_101106
        Misdelivery_403115= getTestingValue.Reading_101106
        Misdelivery_405115= getTestingValue.Reading_101106
        Misdelivery_103118= getTestingValue.Reading_101106
        Misdelivery_110118= getTestingValue.Reading_101106
        Misdelivery_303118= getTestingValue.Reading_101106
        Misdelivery_305118= getTestingValue.Reading_101106
        Misdelivery_403118= getTestingValue.Reading_101106
        Misdelivery_405118= getTestingValue.Reading_101106
        Misdelivery_101105= getTestingValue.Reading_101106
        Misdelivery_110105= getTestingValue.Reading_101106
        Misdelivery_303105= getTestingValue.Reading_101106
        Misdelivery_305105= getTestingValue.Reading_101106
        Misdelivery_103109= getTestingValue.Reading_101106
        Misdelivery_110109= getTestingValue.Reading_101106
        Misdelivery_303109= getTestingValue.Reading_101106
        Misdelivery_305109= getTestingValue.Reading_101106
        c6_p11_6= getTestingValue.Reading_101106
        c6_p12_6= getTestingValue.Reading_101106
        c6_p13_6= getTestingValue.Reading_101106
        c6_p14_6= getTestingValue.Reading_101106
        c6_p15_6= getTestingValue.Reading_101106
        c6_p16_6= getTestingValue.Reading_101106
        c6_p17_6= getTestingValue.Reading_101106
        c7_p11_6= getTestingValue.Reading_101106
        c7_p12_6= getTestingValue.Reading_101106
        c7_p13_6= getTestingValue.Reading_101106
        c7_p14_6= getTestingValue.Reading_101106
        c7_p15_6= getTestingValue.Reading_101106
        c7_p16_6= getTestingValue.Reading_101106
        c7_p17_6= getTestingValue.Reading_101106
        c8_p11_6= getTestingValue.Reading_101106
        c8_p12_6= getTestingValue.Reading_101106
        c8_p13_6= getTestingValue.Reading_101106
        c8_p14_6= getTestingValue.Reading_101106
        c8_p15_6= getTestingValue.Reading_101106
        c8_p17_6= getTestingValue.Reading_101106
        c8_p18_6= getTestingValue.Reading_101106
        c6_p11_10= getTestingValue.Reading_101106
        c6_p12_10= getTestingValue.Reading_101106
        c6_p13_10= getTestingValue.Reading_101106
        c6_p14_10= getTestingValue.Reading_101106
        c6_p15_10= getTestingValue.Reading_101106
        c6_p16_10= getTestingValue.Reading_101106
        c6_p17_10= getTestingValue.Reading_101106
        c7_p11_10= getTestingValue.Reading_101106
        c7_p12_10= getTestingValue.Reading_101106
        c7_p13_10= getTestingValue.Reading_101106
        c7_p14_10= getTestingValue.Reading_101106
        c7_p15_10= getTestingValue.Reading_101106
        c7_p16_10= getTestingValue.Reading_101106
        c7_p17_10= getTestingValue.Reading_101106
        c8_p11_10= getTestingValue.Reading_101106
        c8_p12_10= getTestingValue.Reading_101106
        c8_p13_10= getTestingValue.Reading_101106
        c8_p14_10= getTestingValue.Reading_101106
        c8_p15_10= getTestingValue.Reading_101106
        c8_p17_10= getTestingValue.Reading_101106
        c8_p18_10= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p11_6= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p12_6= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p13_6= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p14_6= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p15_6= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p16_6= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p17_6= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p11_6= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p12_6= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p13_6= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p14_6= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p15_6= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p16_6= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p17_6= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p11_6= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p12_6= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p13_6= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p14_6= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p15_6= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p17_6= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p18_6= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p11_10= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p12_10= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p13_10= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p14_10= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p15_10= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p16_10= getTestingValue.Reading_101106
        imrt_misdelivery_c6_p17_10= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p11_10= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p12_10= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p13_10= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p14_10= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p15_10= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p16_10= getTestingValue.Reading_101106
        imrt_misdelivery_c7_p17_10= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p11_10= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p12_10= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p13_10= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p14_10= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p15_10= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p17_10= getTestingValue.Reading_101106
        imrt_misdelivery_c8_p18_10= getTestingValue.Reading_101106'''


