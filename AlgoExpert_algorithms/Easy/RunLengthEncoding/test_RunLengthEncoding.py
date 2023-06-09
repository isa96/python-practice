'''
Unittests for RunLengthEncoding.py
'''

import unittest
import RunLengthEncoding

class test_RunLengthEncoding(unittest.TestCase):    
    '''
    Class with unittests for RunLegthEncoding.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_str  = "AAAAAAAAAAAAABBCCCCDD"
        output = RunLengthEncoding.runLengthEncoding(input_str)
        self.assertEqual(output, "9A4A2B4C2D")
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()