import unittest
from fibonacci import fibonacci

class TestDP(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(3), 2)

if __name__ == '__main__':
    unittest.main()