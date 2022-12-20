"""
Chris Flodstrom
czf0038
Assignment 04-01
"""

import unittest
import RCube.info as info


class Test(unittest.TestCase):


    def test100_010_ShouldReturnMyUserName(self):
        expectedResult = {'user' : 'czf0038'}
        parms = {'op' : 'info'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)

