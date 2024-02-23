import unittest
import os
import csv
from faker import Faker
from generate import generate_fake_data


class TestGenerateFakeData(unittest.TestCase):
    """Test generate fake data"""

    def setUp(self):
        self.fake = Faker()
        self.filenames = []

    def tearDown(self):
        # Delete files created by the test after tests finished
        for filename in self.filenames:
            os.remove(filename)

    def test_generate_fake_data(self):
        filename = "test_file.csv"
        num_rows = 10
        generate_fake_data(filename, num_rows)
        self.assertTrue(os.path.exists(filename))

        # Check that the file is not empty and contains the expected number of lines
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), num_rows + 1)  # +1 for the header

        # Check that headers in the file match the expected ones
        expected_fieldnames = [
            "Name",
            "Surname",
            "Address",
            "Email",
            "Phone",
            "Date of birth",
            "Profession",
            "Company",
            "Country",
            "City",
        ]
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.assertEqual(reader.fieldnames, expected_fieldnames)

        # Check that every line contains data
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                for field in expected_fieldnames:
                    self.assertTrue(row[field])

        self.filenames.append(filename)


if __name__ == "__main__":
    unittest.main()
