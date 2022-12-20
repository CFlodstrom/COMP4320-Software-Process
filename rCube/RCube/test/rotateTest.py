"""
Chris Flodstrom
czf0038
Assignment 07-01

"""

import unittest
import RCube.rotate as rotate
#import RCube.rotate as rotate


class Test(unittest.TestCase):
    
#bringing over from rotate function
    def test100_130_EmptyCube(self):
        expectedResult = {'status': 'error: Cube is empty'}
        parms = {'cube': ''}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_140_MissingIntegrity(self):
        expectedResult = {'status': 'error: Cube does not have integrity key'}
        parms = {'cube': '111111111222222222333333333444444444555555555666666666'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)


    def test100_010_MissingCubeParameter(self):
        expectedResult = {'status': 'error: missing cube parameter'}
        parms = {'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_150_NotEnoughDigits(self):
        expectedResult = {'status': 'error: Incorrect number of elements, needs to be 54'}
        parms = {'cube': '11111111122222222233333333344444444455555555566666666', 'integrity': '825E9253B6D7DB91050DA156E2CF524AE9B532B0C9C3DF89B01F18592850D5D3'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_160_MissingCubeKey(self):
        expectedResult = {'status': 'error: missing cube parameter'}
        parms = {'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_170_MoreThan6UniqueElements(self):
        expectedResult = {'status': 'error: needs 6 unique elements'}
        parms = {'cube': '111111111222222222333333333444444444555555555111111111', 'integrity': '93C6A03A7B2F9F5D319128523FA96AB3C748C67EAA6FDD4DAC8311F4D0393921'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_180_rotate9Elements(self):
        expectedResult = {'status': 'error: needs 9 colors'}
        parms = {'cube': '111111111222222222333333333444444444555555555666666665', 'integrity': 'FFFA07BE4BF1438C0C660DE9E9C0624640DC23856E875F6730F6195CEAF2AB61'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_190_NoMiddleElements(self):
        expectedResult = {'status': 'error: needs distinct middle numbers'}
        parms = {'cube': '111141111222222222333333333144444444555555555666666666', 'integrity': '0628732992F58A84A7F291067AB6CC9DC9B1AD8428DC93EE5126B0CD88108B0E'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)                
                 
    def test100_230_ImpossibleCorner(self):
        expectedResult = {'status': 'error: impossible corner'}
        parms = {'cube': 'bbgbbbbbbwoooooooogogggggggrrrrrrrrrwwwwwwwwbyyyyyyyyy', 'integrity': '573D39853F85AFD6E55A0760EFA1EBE8A7EACA41753055D9B41D0B3FC5C2E986'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)  
#     
    def test100_240_ImpossibleEdge(self):
        expectedResult = {'status': 'error: impossible edge'}
        parms = {'cube': 'gggggggggrrrrrrrrrbbbbbbbybooooooooowwwwwwwwwybyyyyyyy', 'integrity': '96DDC169F9D847DC098BA3805C1AD55B088293F0138D7D1603C03543F7D5589E'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult) 
                            
        
        
    #could leave an issue when debugging... has same test for cube parameter
#    def test100_020_MissingFaceParameter(self):
#        expectedResult = {'status': 'error: missing face parameter'}
#        parms = {'integrity': ''}
#        actualResult = rotate._rotate(parms)
#        self.assertDictEqual(expectedResult, actualResult)


    def test100_030_TestRotationf(self):
        expectedResult = {'status': 'rotated', 'cube':'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy', 'integrity':'0F3BDBE402C16D85756959CDEE1649281296A8507CDDF29EC328C72CC758DA28'}
        parms = {'side': 'f', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_040_TestRotationF(self):
        expectedResult = {'status': 'rotated', 'cube':'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy', 'integrity':'40C2BD2C76A2F307F760FEB0FAE3352809840F76BD8974613E2BA3B11AFC395E'}
        parms = {'side': 'F', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_050_TestRotationb(self):
        expectedResult = {'status': 'rotated', 'cube':'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo', 'integrity':'660FDE671B5BEA48B0111447BA18EBB728F3F9A4AE10813AAFAE294CD04652DD'}
        parms = {'side': 'b', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_060_TestRotationB(self):
        expectedResult = {'status': 'rotated', 'cube':'gggggggggrrwrrwrrwbbbbbbbbbyooyooyooooowwwwwwyyyyyyrrr', 'integrity':'B38E19C30B88E65EECE3D7CCA4A963F06C99D3F5C4E32F8D76611BB1A9BCADDA'}
        parms = {'side': 'B', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_070_TestRotationr(self):
        expectedResult = {'status': 'rotated', 'cube':'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb', 'integrity':'52F7A03F6CCD1422952F5DF17DE880B41EC309427339A2DAC0A8E114EFAE3F7B'}
        parms = {'side': 'r', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_080_TestRotationR(self):
        expectedResult = {'status': 'rotated', 'cube':'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg', 'integrity':'0BC487F537509ACECE983337A0B682902129D2803AA6E9700F1035511DCE22A6'}
        parms = {'side': 'R', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_090_TestRotationl(self):
        expectedResult = {'status': 'rotated', 'cube':'wggwggwggrrrrrrrrrbbybbybbyooooooooobwwbwwbwwgyygyygyy', 'integrity':'BB960DFCBFE7BCFCA3BE95A22FFD088DB492FB942EB3EC5EE750FAD272330DB0'}
        parms = {'side': 'l', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_090_TestRotationL(self):
        expectedResult = {'status': 'rotated', 'cube':'yggyggyggrrrrrrrrrbbwbbwbbwooooooooogwwgwwgwwbyybyybyy', 'integrity':'3BE670BD7D442CAD986B42CFBC913695C4D666364208B723814DB1F8A3C5DA68'}
        parms = {'side': 'L', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_100_TestRotationt(self):
        expectedResult = {'status': 'rotated', 'cube':'rrrggggggbbbrrrrrrooobbbbbbgggoooooowwwwwwwwwyyyyyyyyy', 'integrity':'0F91C6D401C276775A580869A8BFFC660BF45B134493D77F819636DA29612916'}
        parms = {'side': 't', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_110_TestRotationT(self):
        expectedResult = {'status': 'rotated', 'cube':'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy', 'integrity':'C2541978094B8FF38D7F143F1E3608F90565CF6501215D597E7E3DDD5D4F65B4'}
        parms = {'side': 'T', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_110_TestRotationu(self):
        expectedResult = {'status': 'rotated', 'cube':'ggggggooorrrrrrgggbbbbbbrrroooooobbbwwwwwwwwwyyyyyyyyy', 'integrity':'41B16B12A06F65615143AB4AC653F65B4B599A4C5FE87AB4C879CDEB742FF301'}
        parms = {'side': 'u', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_120_TestRotationU(self):
        expectedResult = {'status': 'rotated', 'cube':'ggggggrrrrrrrrrbbbbbbbbbooooooooogggwwwwwwwwwyyyyyyyyy', 'integrity':'6FCD2F0E5F44AB2BBA6F84A5BCECDD4DA0C9E2CEA96A36EEF72529695F230D25'}
        parms = {'side': 'U', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_190_MissingSideParam(self):
        expectedResult = {'status': 'error: the side cannot be found'}
        parms = {'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)



    
    
    
        