import unittest
from classes.validator import Validator

class TestValidator(unittest.TestCase):

    def test(self):
        # Assume
        facilityname_is_valid = 'African Bush Elephant'
        validator = Validator();

        # Action
        result = validator.FacilityName_is_valid(facilityname_is_valid)

        # Assert
        self.assertFalse(result)

