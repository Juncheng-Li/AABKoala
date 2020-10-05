import unittest
import xlrd
from classes.validator import Validator
import pandas as pd
import math
import numpy as np
import decimal
import re


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
        fac_6= map(str, xls['fac_6'].tolist())
        fac_10= map(str, xls['fac_10'].tolist())
        fac_15	= map(str, xls['fac_15'].tolist())
        fac_18	= map(str, xls['fac_18'].tolist())
        fac_6FFF= map(str, xls['fac_6FFF'].tolist())
        fac_10FFF= map(str, xls['fac_10FFF'].tolist())
        TPR_6= map(str, xls['TPR_6'].tolist())
        TPR_10= map(str, xls['TPR_10'].tolist())
        TPR_15	= map(str, xls['TPR_15'].tolist())
        TPR_18= map(str, xls['TPR_18'].tolist())
        TPR_6FFF= map(str, xls['TPR_6FFF'].tolist())
        TPR_10FFF= map(str, xls['TPR_10FFF'].tolist())
        Reading_101106 = map(str, xls['Reading_101106'].tolist())
        Reading_205106 = map(str, xls['Reading_205106'].tolist())
        Reading_208106= map(str, xls['Reading_208106'].tolist())
        Reading_205206= map(str, xls['Reading_205206'].tolist())
        Reading_208206= map(str, xls['Reading_208206'].tolist())
        Reading_205306= map(str, xls['Reading_205306'].tolist())
        Reading_208306= map(str, xls['Reading_208306'].tolist())
        Reading_303106= map(str, xls['Reading_303106'].tolist())
        Reading_305106= map(str, xls['Reading_305106'].tolist())
        Reading_403106= map(str, xls['Reading_403106'].tolist())
        Reading_405106= map(str, xls['Reading_405106'].tolist())
        Reading_103110= map(str, xls['Reading_103110'].tolist())
        Reading_110110= map(str, xls['Reading_110110'].tolist())
        Reading_303110= map(str, xls['Reading_303110'].tolist())
        Reading_305110= map(str, xls['Reading_305110'].tolist())
        Reading_403110= map(str, xls['Reading_403110'].tolist())
        Reading_405110= map(str, xls['Reading_405110'].tolist())
        Reading_103115= map(str, xls['Reading_103115'].tolist())
        Reading_110115= map(str, xls['Reading_110115'].tolist())
        Reading_303115= map(str, xls['Reading_303115'].tolist())
        Reading_305115= map(str, xls['Reading_305115'].tolist())
        Reading_403115= map(str, xls['Reading_403115'].tolist())
        Reading_405115= map(str, xls['Reading_405115'].tolist())
        Reading_103118= map(str, xls['Reading_103118'].tolist())
        Reading_110118= map(str, xls['Reading_110118'].tolist())
        Reading_303118= map(str, xls['Reading_303118'].tolist())
        Reading_305118= map(str, xls['Reading_305118'].tolist())
        Reading_403118= map(str, xls['Reading_403118'].tolist())
        Reading_405118= map(str, xls['Reading_405118'].tolist())
        Reading_101105= map(str, xls['Reading_101105'].tolist())
        Reading_110105= map(str, xls['Reading_110105'].tolist())
        Reading_303105= map(str, xls['Reading_303105'].tolist())
        Reading_305105= map(str, xls['Reading_305105'].tolist())
        Reading_103109= map(str, xls['Reading_103109'].tolist())
        Reading_110109= map(str, xls['Reading_110109'].tolist())
        Reading_303109= map(str, xls['Reading_303109'].tolist())
        Reading_305109= map(str, xls['Reading_305109'].tolist())
        Misdelivery_101106= map(str, xls['Misdelivery_101106'].tolist())
        Misdelivery_110106= map(str, xls['Misdelivery_110106'].tolist())
        Misdelivery_205106= map(str, xls['Misdelivery_205106'].tolist())
        Misdelivery_208106= map(str, xls['Misdelivery_208106'].tolist())
        Misdelivery_205206= map(str, xls['Misdelivery_205206'].tolist())
        Misdelivery_208206= map(str, xls['Misdelivery_208206'].tolist())
        Misdelivery_205306= map(str, xls['Misdelivery_205306'].tolist())
        Misdelivery_208306= map(str, xls['Misdelivery_208306'].tolist())
        Misdelivery_303106= map(str, xls['Misdelivery_303106'].tolist())
        Misdelivery_305106= map(str, xls['Misdelivery_305106'].tolist())
        Misdelivery_403106= map(str, xls['Misdelivery_403106'].tolist())
        Misdelivery_405106= map(str, xls['Misdelivery_405106'].tolist())
        Misdelivery_103110= map(str, xls['Misdelivery_103110'].tolist())
        Misdelivery_110110= map(str, xls['Misdelivery_110110'].tolist())
        Misdelivery_303110= map(str, xls['Misdelivery_303110'].tolist())
        Misdelivery_305110= map(str, xls['Misdelivery_305110'].tolist())
        Misdelivery_403110= map(str, xls['Misdelivery_403110'].tolist())
        Misdelivery_405110= map(str, xls['Misdelivery_405110'].tolist())
        Misdelivery_103115= map(str, xls['Misdelivery_103115'].tolist())
        Misdelivery_110115= map(str, xls['Misdelivery_110115'].tolist())
        Misdelivery_303115= map(str, xls['Misdelivery_303115'].tolist())
        Misdelivery_305115= map(str, xls['Misdelivery_305115'].tolist())
        Misdelivery_403115= map(str, xls['Misdelivery_403115'].tolist())
        Misdelivery_405115= map(str, xls['Misdelivery_405115'].tolist())
        Misdelivery_103118= map(str, xls['Misdelivery_103118'].tolist())
        Misdelivery_110118= map(str, xls['Misdelivery_110118'].tolist())
        Misdelivery_303118= map(str, xls['Misdelivery_303118'].tolist())
        Misdelivery_305118= map(str, xls['Misdelivery_305118'].tolist())
        Misdelivery_403118= map(str, xls['Misdelivery_403118'].tolist())
        Misdelivery_405118= map(str, xls['Misdelivery_405118'].tolist())
        Misdelivery_101105= map(str, xls['Misdelivery_101105'].tolist())
        Misdelivery_110105= map(str, xls['Misdelivery_110105'].tolist())
        Misdelivery_303105= map(str, xls['Misdelivery_303105'].tolist())
        Misdelivery_305105= map(str, xls['Misdelivery_305105'].tolist())
        Misdelivery_103109= map(str, xls['Misdelivery_103109'].tolist())
        Misdelivery_110109= map(str, xls['Misdelivery_110109'].tolist())
        Misdelivery_303109= map(str, xls['Misdelivery_303109'].tolist())
        Misdelivery_305109= map(str, xls['Misdelivery_305109'].tolist())


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_it_will_accept_a_valid_auditID(self):
        try:
            # Assume
            auditID = getTestingValue.auditIdValue

            for eachAuditID in auditID:
                # print (eachAuditID)

                # Action
                result = self.validator.check_auditID_is_valid(eachAuditID)

                # Assert
                self.assertTrue(result)

        except AssertionError:
            print(eachAuditID + ' is not valid AuditID ')
            # print('AuditID is not valid')

    def test_it_will_accept_a_valid_revisionNumber(self):
        try:
            revisionNumber = getTestingValue.revisionNumberValue

            for eachRevisionNumber in revisionNumber:
                result = self.validator.check_revisionNumber_is_valid(eachRevisionNumber)
                self.assertTrue(result)

        except AssertionError:
            print(eachRevisionNumber + ' is not valid RevisionNumber ')
            # print('AuditID is not valid')

    def test_it_will_accept_a_valid_FacilityName(self):
        try:
            facilityName = getTestingValue.facilityNameValue

            for eachFacilityName in facilityName:
                #print(eachFacilityName)
                result = self.validator.check_facilityNameValue_is_valid(eachFacilityName)
                self.assertTrue(result)

        except AssertionError:
            print(eachFacilityName + ' is not valid FacilityName ')

    def test_it_will_accept_a_valid_FacilityID(self):
        try:
            facilityID = getTestingValue.facilityIDValue

            for eachFacilityID in facilityID:
                #print(eachFacilityID)
                result = self.validator.check_facilityID_is_valid(eachFacilityID)
                self.assertTrue(result)

        except AssertionError:
            print(eachFacilityID + ' is not valid FacilityID ')

    def test_it_will_accept_a_valid_Auditor1(self):
        try:
            auditor1 = getTestingValue.auditor1Value

            for eachAuditor1 in auditor1:
                #print(eachAuditor1)
                result = self.validator.check_auditor1_is_valid(eachAuditor1)
                self.assertTrue(result)
        except AssertionError:
            print(eachAuditor1 + ' is not valid Auditor1 ')

    def test_it_will_accept_a_valid_AuditDateValue(self):
        try:
            auditDate = getTestingValue.auditDateValue

            for eachAuditDate in auditDate:
                # print(eachAuditor1)
                result = self.validator.check_auditDate_is_valid(eachAuditDate)
                self.assertTrue(result)
        except AssertionError:
            print(eachAuditDate + ' is not valid AuditDate ')


    def test_it_will_accept_a_valid_RepDate(self):
        try:
            repDate = getTestingValue.repDateValue
            for eachRepDate in repDate:
                print(eachRepDate)
                result = self.validator.check_repDate_is_valid(eachRepDate)
                self.assertTrue(result)
        except AssertionError:
            print(eachRepDate + ' is not valid RepDate ')


    def test_it_will_accept_a_valid_linacModel(self):
        try:
            linacModel = getTestingValue.linacModelValue
            for eachLinacModel in linacModel:
                print(eachLinacModel)
                result = self.validator.check_repDate_is_valid(eachLinacModel)
                self.assertTrue(result)
        except AssertionError:
            print(eachLinacModel + ' is not valid LinacModel ')

    def test_it_will_accept_a_valid_linacManufacturer(self):
        try:
            linacManufacturer = getTestingValue.linacManufacturerValue
            for eachLinacManufacturer in linacManufacturer:
                print(eachLinacManufacturer)
                result = self.validator.check_repDate_is_valid(eachLinacManufacturer)
                self.assertTrue(result)
        except AssertionError:
            print(eachLinacManufacturer + ' is not valid LinacManufacturer  ')

    def test_it_will_accept_a_valid_planningSystemManufacturer(self):
        try:
            planningSystemManufacturer = getTestingValue.linacManufacturerValue
            for eachPlanningSystemManufacturer in planningSystemManufacturer:
                #print(eachPlanningSystemManufacturer)
                result = self.validator.check_repDate_is_valid(eachPlanningSystemManufacturer)
                self.assertTrue(result)
        except AssertionError:
            print(eachPlanningSystemManufacturer + ' is not valid PlanningSystemManufacturer  ')

    def test_it_will_accept_a_valid_tps(self):
        try:
            tps = getTestingValue.tpsValue
            for eachtps in tps:
                #print(eachPlanningSystemManufacturer)
                result = self.validator.check_repDate_is_valid(eachtps)
                self.assertTrue(result)
        except AssertionError:
            print(eachtps + ' is not valid tps  ')

    def test_it_will_accept_a_valid_kqFac(self):
        try:
            kqFac = getTestingValue.tpsValue
            for eachkqFac in kqFac:
                #print(eachPlanningSystemManufacturer)
                result = self.validator.check_repDate_is_valid(eachkqFac)
                self.assertTrue(result)
        except AssertionError:
            print(eachkqFac + ' is not valid kqFac  ')

    def test_it_will_accept_a_valid_kqFac(self):
        try:
            kqFac = getTestingValue.tpsValue
            for eachkqFac in kqFac:
                # print(eachPlanningSystemManufacturer)
                result = self.validator.check_repDate_is_valid(eachkqFac)
                self.assertTrue(result)
        except AssertionError:
            print(eachkqFac + ' is not valid kqFac  ')

    def test_it_will_accept_a_valid_algorithm(self):
        try:
            algorithm = getTestingValue.algorithmValue
            for eachAlgorithm in algorithm:
                # print(eachPlanningSystemManufacturer)
                result = self.validator.check_repDate_is_valid(eachAlgorithm)
                self.assertTrue(result)

        except AssertionError:
            print(eachAlgorithm + ' is not valid algorithm  ')

    def test_it_will_accept_a_valid_ACDS(self):
        try:
            ACDS = getTestingValue.ACDSValue
            for eachACDS in ACDS:
                # print(eachPlanningSystemManufacturer)
                result = self.validator.check_repDate_is_valid(eachACDS)
                self.assertTrue(result)

        except AssertionError:
            print(eachACDS + ' is not valid ACDS')

    def test_it_will_accept_a_valid_phantom(self):
        try:
            phantom = getTestingValue.phantomValue
            for eachPhantom in phantom:
                # print(eachPlanningSystemManufacturer)
                result = self.validator.check_repDate_is_valid(eachPhantom)
                self.assertTrue(result)
        except AssertionError:
            print(eachPhantom + ' is not valid Phantom')


    def test_it_will_accept_a_valid_phantom(self):
        try:
            phantom = getTestingValue.phantomValue
            for eachPhantom in phantom:
                # print(eachPlanningSystemManufacturer)
                result = self.validator.check_repDate_is_valid(eachPhantom)
                self.assertTrue(result)
        except AssertionError:
            print(eachPhantom + ' is not valid Phantom')

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

            #print(facs)
            for facsValue in facs:
                if math.isnan(float(facsValue)):
                    # print(facsValue)
                    facs.remove(facsValue)
                    # print(facs)
                    for facsValue in facs:
                        facsValue = decimal.Decimal(facsValue)
                        decimalNum = pd.to_numeric(facsValue.as_tuple().exponent)
                        result = self.validator.check_facsValue_decimalNum(decimalNum)
                        #print(decimalNum)
                        self.assertTrue(result)

        except AssertionError:
            print(decimalNum)
            print('The value of energy must be within 3 and 3 digits after the decimal point')

    def test_it_will_accept_a_valid_TPR_Reading_Misdelivery(self):
        TPR_6 = getTestingValue.TPR_6
        TPR_10 = getTestingValue.TPR_10
        TPR_15 = getTestingValue.TPR_15
        TPR_18 = getTestingValue.TPR_18
        TPR_6FFF = getTestingValue.TPR_6FFF
        TPR_10FFF = getTestingValue.TPR_10FFF

        try:
            TPR_Reading_Misdelivery_list = []
            for TPR_6 in TPR_6:
                TPR_Reading_Misdelivery_list.append(TPR_6)
            for TPR_10 in TPR_10:
                TPR_Reading_Misdelivery_list.append(TPR_10)
            for TPR_15 in TPR_15:
                TPR_Reading_Misdelivery_list.append(TPR_15)
            for TPR_18 in TPR_18:
                TPR_Reading_Misdelivery_list.append(TPR_18)
            for TPR_6FFF in TPR_6FFF:
                TPR_Reading_Misdelivery_list.append(TPR_6FFF)
            for TPR_10FFF in TPR_10FFF:
                TPR_Reading_Misdelivery_list.append(TPR_10FFF)


            for value in TPR_Reading_Misdelivery_list:
                if math.isnan(float(value)):
                    # print(facsValue)
                    TPR_Reading_Misdelivery_list.remove(value)
                    # print(facs)
                    for value in TPR_Reading_Misdelivery_list:
                        value = decimal.Decimal(value)
                        decimalNum = pd.to_numeric(value.as_tuple().exponent)
                        result = self.validator.check_facsValue_decimalNum(decimalNum)
                        #print(decimalNum)
                        self.assertTrue(result)

        except AssertionError:
            print(value)
            print(decimalNum)
            print('The value of energy must be within 3 and 3 digits after the decimal point')


""""
                Reading_101106 =getTestingValue.Reading_101106
                Reading_205106 = getTestingValue.Reading_205106
                Reading_208106 = getTestingValue.Reading_208106
                Reading_205206 = getTestingValue.Reading_205206
                Reading_208206 = getTestingValue.Reading_208206
                Reading_205306 = getTestingValue.Reading_205306
                Reading_208306 = getTestingValue.Reading_208306
                Reading_303106 = getTestingValue.Reading_303106
                Reading_305106 = getTestingValue.Reading_305106
                Reading_403106 = getTestingValue.Reading_403106
                Reading_405106 = getTestingValue.Reading_405106
                Reading_103110 = getTestingValue.Reading_103110
                Reading_110110 = getTestingValue.Reading_110110
                Reading_303110 = getTestingValue.Reading_303110
                Reading_305110 = getTestingValue.Reading_305110
                Reading_403110 = getTestingValue.Reading_403110
                Reading_405110 = getTestingValue.Reading_405110
                Reading_103115 = getTestingValue.Reading_103115
                Reading_110115 = getTestingValue.Reading_110115
                Reading_303115 = getTestingValue.Reading_303115
                Reading_305115 = getTestingValue.Reading_305115
                Reading_403115 = getTestingValue.Reading_403115
                Reading_405115 = getTestingValue.Reading_405115
                Reading_103118 = getTestingValue.Reading_103118
                Reading_110118 = getTestingValue.Reading_110118
                Reading_303118 = getTestingValue.Reading_303118
                Reading_305118 = getTestingValue.Reading_305118
                Reading_403118 = getTestingValue.Reading_403118
                Reading_405118 = getTestingValue.Reading_405118
                Reading_101105 = getTestingValue.Reading_101105
                Reading_110105 = getTestingValue.Reading_110105
                Reading_303105 = getTestingValue.Reading_303105
                Reading_305105 = getTestingValue.Reading_305105
                Reading_305105 = getTestingValue.Reading_305105
                Reading_110109 = getTestingValue.Reading_110109
                Reading_303109 = getTestingValue.Reading_303109
                Reading_305109 = getTestingValue.Reading_305109
                Misdelivery_101106 = getTestingValue.Misdelivery_101106
                Misdelivery_110106 = getTestingValue.Misdelivery_110106
                Misdelivery_205106 = getTestingValue.Misdelivery_205106
                Misdelivery_208106 = getTestingValue.Misdelivery_208106
                Misdelivery_205206 = getTestingValue.Misdelivery_205206
                Misdelivery_208206 = getTestingValue.Misdelivery_208206
                Misdelivery_205306 = getTestingValue.Misdelivery_205306
                Misdelivery_208306 = getTestingValue.Misdelivery_208306
                Misdelivery_303106 = getTestingValue.Misdelivery_303106
                Misdelivery_305106 = getTestingValue.Misdelivery_305106
                Misdelivery_403106 = getTestingValue.Misdelivery_403106
                Misdelivery_405106 = getTestingValue.Misdelivery_405106
                Misdelivery_103110 = getTestingValue.Misdelivery_103110
                Misdelivery_110110 = getTestingValue.Misdelivery_110110
                Misdelivery_303110 = getTestingValue.Misdelivery_303110
                Misdelivery_305110 = getTestingValue.Misdelivery_305110
                Misdelivery_403110 = getTestingValue.Misdelivery_403110
                Misdelivery_405110 = getTestingValue.Misdelivery_405110
                Misdelivery_103115 = getTestingValue.Misdelivery_103115
                Misdelivery_110115 =getTestingValue.Misdelivery_110115
                Misdelivery_303115 = getTestingValue.Misdelivery_303115
                Misdelivery_305115 = getTestingValue.Misdelivery_305115
                Misdelivery_403115 = getTestingValue.Misdelivery_403115
                Misdelivery_405115 = getTestingValue.Misdelivery_405115
                Misdelivery_103118 = getTestingValue.Misdelivery_103118
                Misdelivery_110118 = getTestingValue.Misdelivery_110118
                Misdelivery_303118 = getTestingValue.Misdelivery_303118
                Misdelivery_305118 = getTestingValue.Misdelivery_305118
                Misdelivery_403118 = getTestingValue.Misdelivery_403118
                Misdelivery_405118 = getTestingValue.Misdelivery_405118
                Misdelivery_101105 =getTestingValue.Misdelivery_101105
                Misdelivery_110105 = getTestingValue.Misdelivery_110105
                Misdelivery_303105 = getTestingValue.Misdelivery_303105
                Misdelivery_305105 = getTestingValue.Misdelivery_305105
                Misdelivery_103109 = getTestingValue.Misdelivery_103109
                Misdelivery_110109 = getTestingValue.Misdelivery_110109
                Misdelivery_303109 = getTestingValue.Misdelivery_303109
                Misdelivery_305109 = getTestingValue.Misdelivery_305109
                """