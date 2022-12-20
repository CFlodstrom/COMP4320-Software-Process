"""
Chris Flodstrom
czf0038
Assignment 04-01
"""

import unittest
import RCube.create as create


class Test(unittest.TestCase):


    def test100_010_NominalFaceValue(self):
        expectedResult = {'cube' : '111111111222222222333333333444444444555555555666666666', 'integrity' : '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED', 'status' : 'ok'}
        parms = {'faces': '123456'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_020_NoFaceValue(self):
        expectedResult = {'cube' : 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 'status' : 'ok'}
        parms = {'faces' : ''}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
         
    def test100_030_MissingFaces(self):
        expectedResult = {'cube' : 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 'status' : 'ok'}
        parms = {'create' : ''}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
         
    def test100_040_extraneousParms(self):
        expectedResult = {'cube' : 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 'status' : 'ok'}
        parms = {'create&f' : '123456'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_910_IncorrectLengthForFaces(self):
        expectedResult = {'status': 'error: There is an invalid length of faces'}
        parms = {'faces' : '1234567'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_920_DuplicateItem(self):
        expectedResult = {'status': 'error: There is a duplicate number'}
        parms = {'faces' : '113456'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_930_NotEnoughFaces(self):
        expectedResult = {'status': 'error: There is an invalid length of faces'}
        parms = {'faces' : '12345'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
