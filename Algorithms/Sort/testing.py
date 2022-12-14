import unittest
from radix_sort import radix_sort
from quick_sort import quick_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

class TestSortingAlgos(unittest.TestCase):
    def test_bubble(self):
        print('Testing Bubble Sort')
        self.assertEqual(bubble_sort([3, 2]), [2, 3])
        self.assertEqual(bubble_sort([5, 532, 5, 252, 56, 653, 876, 89, 1, 4]), [1, 4, 5, 5, 56, 89, 252, 532, 653, 876])
        self.assertEqual(bubble_sort([5, 4, 4, 3, 2, 1]), [1, 2, 3, 4, 4, 5])

    def test_merge(self):
        print('\nTesting Merge Sort')
        self.assertEqual(merge_sort([3, 2]), [2, 3])
        self.assertEqual(merge_sort([5, 532, 5, 252, 56, 653, 876, 89, 1, 4]), [1, 4, 5, 5, 56, 89, 252, 532, 653, 876])
        self.assertEqual(merge_sort([5, 4, 4, 3, 2, 1]), [1, 2, 3, 4, 4, 5])

    def test_selection(self):
        print('\nTesting Selection Sort')
        self.assertEqual(selection_sort([3, 2]), [2, 3])
        self.assertEqual(selection_sort([5, 532, 5, 252, 56, 653, 876, 89, 1, 4]), [1, 4, 5, 5, 56, 89, 252, 532, 653, 876])
        self.assertEqual(selection_sort([5, 4, 4, 3, 2, 1]), [1, 2, 3, 4, 4, 5])
    
    def test_insertion(self):
        print('\nTesting Selection Sort')
        self.assertEqual(insertion_sort([3, 2]), [2, 3])
        self.assertEqual(insertion_sort([5, 532, 5, 252, 56, 653, 876, 89, 1, 4]), [1, 4, 5, 5, 56, 89, 252, 532, 653, 876])
        self.assertEqual(insertion_sort([5, 4, 4, 3, 2, 1]), [1, 2, 3, 4, 4, 5])

    def test_quick(self):
        print('\nTesting Quick Sort')
        array = [5, 4, 4, 3, 2, 1]
        quick_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3, 4, 4, 5])
    
    def test_radix(self):
        print('\nTesting Radix Sort')
        self.assertEqual(radix_sort([3, 2]), [2, 3])
        self.assertEqual(radix_sort([5, 532, 5, 252, 56, 653, 876, 89, 1, 4]), [1, 4, 5, 5, 56, 89, 252, 532, 653, 876])
        self.assertEqual(radix_sort([5, 4, 4, 3, 2, 1]), [1, 2, 3, 4, 4, 5])

if __name__ == '__main__':
    unittest.main()