'''
Unittests for QuickSort.py
'''

import unittest
import QuickSort

class test_QuickSort(unittest.TestCase):
    '''
    Class contains unittests for QuickSort.py
    '''
 
    def test_TestOutputArray(self):
        '''
        Checks if array is sorted.
        '''
        output = QuickSort.QuickSort([3,4,2,5,1])
        self.assertEqual(output, [1,2,3,4,5])

    def test_CorrectInput(self):
        '''
        Checks if input is correct.
        '''
        output = QuickSort.QuickSort(123)
        self.assertEqual(output, -1)

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()