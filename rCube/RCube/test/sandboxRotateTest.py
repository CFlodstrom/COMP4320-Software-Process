'''
Created on Nov 30, 2020

@author: chrisflodstrom
'''
import unittest
import RCube.sandbox.sandboxRotate as sand

class Test(unittest.TestCase):

    def test100_010_IfNoMatchIntegrityString(self):
        expectedResult = {'cube': 'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy', 'integrity': '6FCD2F0E5F44AB2BBA6F84A5BCECDD4DA0C9E2CEA96A36EEF72529695F230D25'}
        parms = {'cube': 'ggggggrrrrrrrrrbbbbbbbbbooooooooogggwwwwwwwwwyyyyyyyyy'}
        actualResult = sand._sandbox(parms)
        self.assertDictEqual(expectedResult, actualResult)
