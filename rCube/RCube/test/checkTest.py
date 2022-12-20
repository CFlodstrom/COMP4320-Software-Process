"""
Chris Flodstrom
czf0038
Assignment 07-01

"""

import unittest
import RCube.check as check


class Test(unittest.TestCase):

      
    def test100_010_EmptyCube(self):
        expectedResult = {'status': 'error: Cube is empty'}
        parms = {'cube': ''}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_020_NotEnoughDigits(self):
        expectedResult = {'status': 'error: Incorrect number of elements, needs to be 54'}
        parms = {'cube': '11111111122222222233333333344444444455555555566666666', 'integrity': '825E9253B6D7DB91050DA156E2CF524AE9B532B0C9C3DF89B01F18592850D5D3'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_040_MissingCubeKey(self):
        expectedResult = {'status': 'error: missing cube parameters'}
        parms = {'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
                 
        
    def test100_030_MoreThan6UniqueElements(self):
        expectedResult = {'status': 'error: needs 6 unique elements'}
        parms = {'cube': '111111111222222222333333333444444444555555555111111111', 'integrity': '93C6A03A7B2F9F5D319128523FA96AB3C748C67EAA6FDD4DAC8311F4D0393921'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
            
    def test100_040_CheckFull(self):
        expectedResult = {'status': 'full'}
        parms = {'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
# # 
    def test100_050_Check9Elements(self):
        expectedResult = {'status': 'error: needs 9 colors'}
        parms = {'cube': '111111111222222222333333333444444444555555555666666665', 'integrity': 'FFFA07BE4BF1438C0C660DE9E9C0624640DC23856E875F6730F6195CEAF2AB61'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_060_NoMiddleElements(self):
        expectedResult = {'status': 'error: needs distinct middle numbers'}
        parms = {'cube': '111141111222222222333333333144444444555555555666666666', 'integrity': '0628732992F58A84A7F291067AB6CC9DC9B1AD8428DC93EE5126B0CD88108B0E'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_070_CheckSpots(self):
        expectedResult = {'status': 'spots'}
        parms = {'cube': 'rrrrbrrrryyyyryyyyoooogoooowwwwowwwwbbbbybbbbggggwgggg', 'integrity': '8BE0EEDF13B2B464A2C7A120E6104AC7039B758E93D6F65651616FBBEED9A1EF'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)                     
# 
    def test100_080_CheckCrosses(self):
        expectedResult = {'status': 'crosses'}
        parms = {'cube': 'ybybbbybybrbrrrbrbwgwgggwgwgogooogogryryyyryrowowwwowo', 'integrity': '3A2CA2368EDAB67D1EAB30A5DCA67757FC389AC2924E3EDAB522BAABF8403202'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)  
#         
         
    def test100_090_StatusUnknown(self):
        expectedResult = {'status': 'unknown'}
        parms = {'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)  
        
#         
    def test100_100_ImpossibleCorner(self):
        expectedResult = {'status': 'error: impossible corner'}
        parms = {'cube': 'bbgbbbbbbwoooooooogogggggggrrrrrrrrrwwwwwwwwbyyyyyyyyy', 'integrity': '573D39853F85AFD6E55A0760EFA1EBE8A7EACA41753055D9B41D0B3FC5C2E986'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)  
#     
    def test100_110_ImpossibleEdge(self):
        expectedResult = {'status': 'error: impossible edge'}
        parms = {'cube': 'gggggggggrrrrrrrrrbbbbbbbybooooooooowwwwwwwwwybyyyyyyy', 'integrity': '96DDC169F9D847DC098BA3805C1AD55B088293F0138D7D1603C03543F7D5589E'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult) 
                            

        




          

