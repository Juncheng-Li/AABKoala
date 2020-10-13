import datetime

import pandas
import math


class Validator:
    """ Validate auditID"""""
    """no space presented between auditID, the length of auditID should less and equal to 4, auditID only contain 
    numbers  """

    def check_auditID_is_valid(self, auditID):

        # auditID = '0000'
        # check if space between auditID.
        if ' ' in auditID:
            return False  # if auditID have space is ture, so return False, AssertFalse is true

        if len(auditID) > 4:
            return False

        if not auditID.isdecimal():
            return False

        return True  # if auditID have space is false, return true, AssertTure is true

    """ RevisionNumber only contain numbers revisionNumber_is_valid"""""

    def check_revisionNumber_is_valid(self, revisionNumber):

        if not revisionNumber.isdecimal():
            return False

        if revisionNumber is None:
            return False
        return True  # if auditID have space is false, return true, AssertTure is true

    """ facilityName should not none or less than 4 character"""""

    def check_facilityNameValue_is_valid(self, facilityName):
        if len(facilityName) < 4:
            return False
        return True  # if auditID have space is false, return true, AssertTure is true

    """ facilityID should not none"""""

    def check_facilityID_is_valid(self, facilityName):
        if facilityName == '' or math.isnan(float(facilityName)):
            return False
        return True
        # regular expression check.TBC..

    """ Auditor1 should not none"""""

    def check_auditor1_is_valid(self, auditor1):
        if auditor1 == '' or math.isnan(float(auditor1)):
            return False
        return True

    """ auditDate should not none"""""

    def check_auditDate_is_valid(self, auditDate):
        if len(auditDate) < 4:
            return False
        return True

    """ repDate should not none"""""

    def check_repDate_is_valid(self, repDate):
        if repDate == '' or math.isnan(float(repDate)):
            return False
        return True

    def check_facsValue_decimalNum(self, decimalNum):
        if decimalNum < -3:
            return False