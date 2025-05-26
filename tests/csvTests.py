import unittest
import csv

class TestCsvFile(unittest.TestCase):
    
    def test_csv_has_12_columns(self):
        expected_column = 12
        file_path = "profiles1.csv"

        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            actual_column_count = len(header)

        self.assertEqual(actual_column_count, expected_column)

    def test_csv_has_900_rows(self):
        expected_min_row_count = 900
        file_path = "profiles1.csv"

        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            data_rows = list(reader)
            actual_column_count = len(data_rows) 

        self.assertGreaterEqual(actual_column_count, expected_min_row_count)
    

    if __name__ == "__main__":
        unittest.main()

