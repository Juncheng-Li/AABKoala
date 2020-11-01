import math


class Validator:
    """ Validate auditID"""""
    """no space presented between auditID, the length of auditID should less and equal to 4, auditID only contain 
    numbers  """

    def check_auditID_is_valid(self, auditID):
        # check if space between auditID.
        if auditID == '':
            return False
        if ' ' in auditID:
            return False  # if auditID have space is ture, so return False, AssertFalse is true
        if len(auditID) < 4:
            return False
        if len(auditID) > 4:
            return False
        return True  # if auditID have space is false, return true, AssertTure is true

    """ facilityName should not none or less than 4 character"""""
    def check_facilityNameValue_is_valid(self, facilityName):
        if facilityName == '':
            return False

        if len(facilityName) < 4:
            return False
        return True  # if auditID have space is false, return true, AssertTure is true

    """ RevisionNumber only contain numbers revisionNumber_is_valid """

    def check_revisionNumber_is_valid(self, revisionNumber):
        if ' ' in revisionNumber:
            return False

        if not revisionNumber.isdecimal():
            return False

        if revisionNumber is None:
            return True
        return True





    """ facilityID should not none"""""

    def check_facilityID_is_valid(self, facilityName):
        if facilityName == '' or math.isnan(float(facilityName)):
            return False

        return True


    """ Auditor1 should not none"""""

    def check_auditor1_is_valid(self, auditor1):
        if auditor1 == '':
            return False
        return True

    """ auditDate should not none"""""

    def check_auditDate_is_valid(self, auditDate):
        if len(auditDate) < 4:
            return False
        return True

    """ repDate should not none"""""

    def check_linacModel_is_valid(self, linacModel):
        if linacModel == '':
            return False
        return True

    def check_facsValue_decimalNum(self, decimalNum):
        if decimalNum < -3:
            return False
        return True

    def check_linacManufacturer_is_valid(self, linacManufacturer):
        # check if space between auditID.
        if linacManufacturer == '':
            return False
        return True

    def check_planningSystemManufacturer_is_valid(self, planningSystemManufacturer):
        # check if space between auditID.
        if planningSystemManufacturer == '':
            return False
        return True

    def check_facsValue_is_valid(self, facsValue):
        if (facsValue.matches("[a-zA-Z]+")):
            return False

        # check if space between auditID.
        if facsValue == '':
            return True

        if ' ' in facsValue:
            return False

        return True