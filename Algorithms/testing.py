import unittest
import sorting

class TestSortingAlgos(unittest.TestCase):
    def test_bubble(self):
        print('Testing Bubble Sort')
        self.assertEqual(sorting.bubble_sort([3, 2, 1]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()