import unittest
from extract import extract_numbers

class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.data = None
        with open(f'test_file.txt', 'r') as file:
            self.data = file.read().replace('\n', '')

    def test_num_extract(self):
        self.assertEqual(extract_numbers('Take immediate action to stop the violation and notify King County Industrial Waste within 24 hours of learning the violation.'), {91: '24'})
        self.assertEqual(extract_numbers('Whenever an effluent check shows a pH violation, as defined in King Country Code 28.84.060.N "Violations," the Permittee shall take immediate steps to bring the discharge back into compliance. If that is not possible, the Permittee shall cease discharge.'), {81: '28', 84: '84', 87: '060'})
        self.assertEqual(extract_numbers('At no time shall two successive reaedings on an explosive hazard meter at the point of discharge into the King Country sewerage system (or at any point in the system) be more than five percent (5%) of the LEL. No single reading shall exceed ten percent (10%) of the LEL.'), { 194: '5', 254: '10'})
        self.assertEqual(extract_numbers(''), {})
        self.assertEqual(extract_numbers('This sentence has no numbers.'), {})
        self.assertTrue(extract_numbers(self.data))

if __name__ == "__main__":
    unittest.main()