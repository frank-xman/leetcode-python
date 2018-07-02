import unittest
from quicksort import *

class TestQuickSort(unittest.TestCase):
    """Test mathfuc.py"""

    def test_quicksort(self):
        """Test method quick(a, b)"""
        self.assertEqual([13, 27, 38, 49, 49, 65, 76, 97], QuickSort([49,38,65,97,76,13,27,49],0,7))
if __name__=='__main__':
    unittest.main()