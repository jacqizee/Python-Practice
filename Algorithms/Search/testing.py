import unittest
from binary_search import binary_search
from linear_search import linear_search

class TestSearchAlgos(unittest.TestCase):
    def test_binary_search(self):
        print('Testing Binary Search')
        self.assertEqual(binary_search([1,2,3,4,5], 3), 2)
        self.assertEqual(binary_search([1,2,3,4,5], 5), 4)
        self.assertEqual(binary_search([1,2,3,4,5], 1), 0)
        self.assertEqual(binary_search([1,2,3,4,5], 25), None)

    def test_linear_search(self):
        print('\nTesting Linear Search')
        self.assertEqual(linear_search([1,2,3,4,5], 3), 2)
        self.assertEqual(linear_search([1,2,3,4,5], 5), 4)
        self.assertEqual(linear_search([1,2,3,4,5], 1), 0)
        self.assertEqual(linear_search([1,2,3,4,5], 25), None)
    
    def test_bfs(self):
        pass

    def test_dfs(self):
        pass

if __name__ == '__main__':
    unittest.main()