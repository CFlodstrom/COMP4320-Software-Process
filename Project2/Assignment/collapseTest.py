#Chris Flodstrom
#czf0038
#Assignment 1

import unittest
import Assignment.collapse as collapse

class CollapseTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #Tests one digit to ensure it collapses properly
    def test100_010_ShouldCollapseOneDigit(self):
        value = '5'
        expectedResult = '5'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        pass
    #Tests two digits to ensure it collapses properly
    def testShouldCollapseTwoDigits(self):
        value = '10'
        expectedResult = '1'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        pass 
    #Tests three digits to ensure it collapses properly       
    def testShouldCollapseThreeDigits(self):
        value = '123'
        expectedResult = '6'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        pass
    
    #Tests five digits to ensure it collapses properly
    def testShouldCollapseFiveDigits(self):
        value = '98769'
        expectedResult = '3'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        pass
    
    #Tests a letter to make sure it returns a value of none
    def testShouldCollapseLetter(self):
        value = 'a'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        pass
    
    #Tests a blank space to ensure it will return a value of none
    def testShouldCollapseNothing(self):
        value = ''
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        pass
    
    #Tests 50 digits to ensure it does not collapse and returns a value of none
    def testShouldCollapseFiftyDigits(self):
        value = '111111111111111111111111111111111111111111111111111'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        pass
    
    #Tests 49 digits to ensure it does not collapse and returns a value of 4
    def testShouldCollapseFortyNineDigits(self):
        value = '1111111111111111111111111111111111111111111111111'
        expectedResult = '4'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        pass
    
    #Tests a non integer to ensure it does not collapse and returns a value of none
    def testShouldCollapseNonInteger(self):
        value = '3.3'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        pass
    
    #Tests a negative number to ensure it does not collapse and returns a value of none
    def testShouldCollapseNegativeNumber(self):
        value = '-1'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        pass
    