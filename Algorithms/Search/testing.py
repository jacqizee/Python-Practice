import unittest
from binary_search import binary_search

class TestSearchAlgos(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([1,2,3,4,5], 3), 2)
        self.assertEqual(binary_search([1,2,3,4,5], 5), 4)
        self.assertEqual(binary_search([1,2,3,4,5], 1), 0)
        self.assertEqual(binary_search([1,2,3,4,5], 25), None)

if __name__ == '__main__':
    unittest.main()