import unittest
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort

class TestSortingAlgos(unittest.TestCase):
    def test_bubble(self):
        print('Testing Bubble Sort')
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])

    def test_merge(self):
        print('\nTesting Merge Sort')
        self.assertEqual(merge_sort([5, 4, 4, 3, 2, 1]), [1, 2, 3, 4, 4, 5])

    def test_selection(self):
        print('\nTesting Selection Sort')
        self.assertEqual(selection_sort([5, 4, 4, 3, 2, 1]), [1, 2, 3, 4, 4, 5])

if __name__ == '__main__':
    unittest.main()