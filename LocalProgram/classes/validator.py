class Validator:

    def FacilityName_is_valid (self, facilityname_is_valid):

        if len(facilityname_is_valid) > 4:
            return False

        if ' ' in facilityname_is_valid:
            return False

        if facilityname_is_valid.islower():
            return False

        return True