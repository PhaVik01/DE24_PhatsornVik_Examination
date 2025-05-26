import unittest
import json

class TestJsonFile(unittest.TestCase):
    def test_if_file_has_required_keys(self):
        file_path = "data.json"
        required_keys = ["Givenname", "Surname", "Streetaddress", "City", "Zipcode",
                         "Country", "CountryCode","NationalId", "TelephoneCountryCode", 
                         "Telephone", "Birthday", "ConsentToContact"]
        
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)

        for row in data:
            for key in required_keys:
                self.assertIn(key, row)

    def test_if_file_has_900_or_more_rows(self):
        file_path = "data.json"
        expected_min_rows = 900

        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            actual_row_count = len(data)

        self.assertGreaterEqual(actual_row_count, expected_min_rows)

    if __name__ == "__main__":
        unittest.main()
