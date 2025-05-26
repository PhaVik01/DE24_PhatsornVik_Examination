
import unittest

from generate import getCountryCode
   
class TestCountryCode(unittest.TestCase):

    def test_if_country_code_is_sv_SE(self):
        input_value= "sv_SE"
        expected = "SE"

        result = getCountryCode(input_value)

        self.assertEqual(result, expected)

    def test_if_country_code_is_no_NO(self):
        input_value = "no_NO"
        expected = "NO"

        result = getCountryCode(input_value)

        self.assertEqual(result, expected)

    def test_if_country_code_is_fi_FI(self):
        input_value = "fi_FI"
        expected = "FI"

        result = getCountryCode(input_value)

        self.assertEqual(result, expected)

    def test_if_country_code_is_dk_DK(self):
        input_value = "dk_DK"
        expected = "XX"

        result = getCountryCode(input_value)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main() 
