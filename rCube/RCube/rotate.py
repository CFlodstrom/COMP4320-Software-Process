"""
Chris Flodstrom
czf0038
Assignment 07-01

"""
import hashlib

def _rotate(parms):

    if 'cube' not in parms:
        return {'status': 'error: missing cube parameter'}
    
    if len(parms['cube']) == 0:
        return {'status': 'error: Cube is empty'} 
      
    if len(parms['cube']) != 54:
        return {'status': 'error: Incorrect number of elements, needs to be 54'}
    
    if not sixElements(parms['cube']):
        return {'status': 'error: needs 6 unique elements'} 

    if not colorChecker(parms['cube']):
        return {'status': 'error: needs 9 colors'} 

    if not checkMiddle(parms['cube']):
        return {'status': 'error: needs distinct middle numbers'}
    
    if not checkCorner(parms['cube']):
        return {'status': 'error: impossible corner'}
 
    if not checkEdges(parms['cube']):
        return {'status': 'error: impossible edge'}
    
    if not 'integrity' in parms:
        return {'status': 'error: Cube does not have integrity key'}
    
    if len(parms['integrity']) == 0:
        return {'status': 'error: does not have integrity value'}
    
    if 'cube' in parms:
        cValue = parms['cube']
        
    if 'integrity' not in parms:
        return {'status': 'error: missing integrity parameter'}
     
    if 'side' not in parms:
        return {'status': 'error: the side cannot be found'}

    if 'side' in parms:
        sValue = parms['side']
        
        if sValue == 'f':
            x = facesf(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}
        
        if sValue == 'F':
            x = facesF(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}
        
        if sValue == 'b':
            x = facesb(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}

        if sValue == 'B':
            x = facesB(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}
        
        if sValue == 'r':
            x = facesr(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}

        if sValue == 'R':
            x = facesR(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}
        
        if sValue == 'l':
            x = facesl(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}

        if sValue == 'L':
            x = facesL(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}
        
        if sValue == 't':
            x = facest(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}         
        
        if sValue == 'T':
            x = facesT(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y} 
        
#70
        if sValue == 'u':
            x = facesu(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}  
        
        if sValue == 'U':
            x = facesU(cValue)
            y = integrity(x)
            return {'status': 'rotated', 'cube': x, 'integrity': y}  
        
        
def sixElements(faces):
    typeColor = []
    for j in range(54):
        if faces[j] not in typeColor:
            typeColor.append(faces[j])
    if len(typeColor) == 6:
        return True
    else:
        return False
    
def colorChecker(faces):
    countingColors ={}
    for i in range(54):
        if faces[i] not in countingColors:
            countingColors[faces[i]] = 1
        elif countingColors[faces[i]] == 9:
            return False 
        else:
            countingColors[faces[i]] = countingColors[faces[i]] + 1
    return True 

def checkMiddle(faces):
    typeColor = []
    for j in range(6):
#100
        val = j * 9
        if faces[val + 4] in typeColor:
            return False
        else:
            typeColor.append(faces[val + 4]) 
    return True 

def checkCorner(faces):
    typeColor = []
    for i in range(6):
        val = i * 9
        typeColor.append(faces[val + 4])
    possibleValue =[[typeColor[0], typeColor[3], typeColor[4]], [typeColor[0], typeColor[1], typeColor[4]], [typeColor[0], typeColor[3], typeColor[5]], [typeColor[0], typeColor[1], typeColor[5]], \
               [typeColor[2], typeColor[1], typeColor[4]], [typeColor[2], typeColor[3], typeColor[4]], [typeColor[2], typeColor[1], typeColor[5]], [typeColor[2], typeColor[3], typeColor[5]]]
    
    actualValue = [[faces[0], faces[29], faces[42]], [faces[2], faces[9], faces[44]], [faces[6], faces[35], faces[45]], [faces[8], faces[15], faces[47]], \
              [faces[18], faces[11], faces[38]], [faces[20], faces[27], faces[36]], [faces[24], faces[17], faces[53]], [faces[26], faces[33], faces[51]]]
    eval = []
    for i in range(len(possibleValue)):
        for j in range(len(actualValue)):
            if j in eval:
                continue
            hold1 = possibleValue[i]
            hold2 = actualValue[j]
            count = 0
            if hold1[0] in hold2:
                count = 1
            if hold1[1] in hold2:
                count += 1
            if hold1[2] in hold2:
                count += 1
            if count == 3:
                eval.append(j)
    if len(eval) == 8:
        return True 
    else: 
        return False 
    
def checkEdges(faces):
    typeColor = []
    for i in range(6):
        val = i * 9
        typeColor.append(faces[val + 4])
    possibleValue =[[typeColor[0], typeColor[4]], [typeColor[0], typeColor[3]], [typeColor[0], typeColor[1]], [typeColor[0], typeColor[5]], [typeColor[2], typeColor[4]], [typeColor[2], typeColor[1]], \
               [typeColor[2], typeColor[3]], [typeColor[2], typeColor[5]], [typeColor[3], typeColor[4]], [typeColor[3], typeColor[5]], [typeColor[1], typeColor[4]], [typeColor[1], typeColor[5]]]
    
    actualValue = [[faces[1], faces[43]], [faces[3], faces[32]], [faces[5], faces[12]], [faces[7], faces[46]], [faces[19], faces[37]], [faces[21], faces[14]], \
              [faces[23], faces[30]], [faces[25], faces[52]], [faces[28], faces[39]], [faces[34], faces[48]], [faces[10], faces[41]], [faces[16], faces[50]]]
    eval = []
    for i in range(len(possibleValue)):
        for j in range(len(actualValue)):
            if j in eval:
                continue
            hold1 = possibleValue[i]
#150
            hold2 = actualValue[j]
            count = 0
            if hold1[0] in hold2:
                count = 1
            if hold1[1] in hold2:
                count += 1
            if count == 2:
                eval.append(j)
    if len(eval) == 12:
        return True 
    else: 
        return False

                     
def facesf(cValue):
    curCube = list(cValue)
    #front
    curCube[0] = cValue[6]
    curCube[1] = cValue[3]
    curCube[2] = cValue[0]
    curCube[3] = cValue[7]
    curCube[4] = cValue[4]
    curCube[5] = cValue[1]
    curCube[6] = cValue[8]
    curCube[7] = cValue[5]
    curCube[8] = cValue[2]
    #top
    curCube[42] = cValue[35]
    curCube[43] = cValue[32]
    curCube[44] = cValue[29]
    #right
    curCube[9] = cValue[42]
    curCube[12] = cValue[43]
    curCube[15] = cValue[44]
    #under
    curCube[45] = cValue[15]
    curCube[46] = cValue[12]
    curCube[47] = cValue[9]
    #left
    curCube[29] = cValue[45]
    curCube[32] = cValue[46]
    curCube[35] = cValue[47]
    finCube = "".join(curCube)
    return finCube

def facesF(cValue):
    curCube = list(cValue)
    #front
    curCube[0] = cValue[2]
    curCube[1] = cValue[5]
    curCube[2] = cValue[8]
    curCube[3] = cValue[1]
    curCube[4] = cValue[4]
    curCube[5] = cValue[7]
    curCube[6] = cValue[0]
    curCube[7] = cValue[3]
    curCube[8] = cValue[6]
    #top
    curCube[42] = cValue[9]
    curCube[43] = cValue[12]
    curCube[44] = cValue[15]
    # 200 right
    curCube[9] = cValue[47]
    curCube[12] = cValue[46]
    curCube[15] = cValue[45]
    #under
    curCube[45] = cValue[29]
    curCube[46] = cValue[32]
    curCube[47] = cValue[35]
    #left
    curCube[29] = cValue[44]
    curCube[32] = cValue[43]
    curCube[35] = cValue[42]
    finCube = "".join(curCube)
    return finCube

def facesb(cValue):
    curCube = list(cValue)
    #front
    curCube[18] = cValue[24]
    curCube[19] = cValue[21]
    curCube[20] = cValue[18]
    curCube[21] = cValue[25]
#    curCube[22] = cValue[19]
    curCube[23] = cValue[19]
    curCube[24] = cValue[26]
    curCube[25] = cValue[23]
    curCube[26] = cValue[20]
    #top
    curCube[36] = cValue[11]
    curCube[37] = cValue[14]
    curCube[38] = cValue[17]
    #right
    curCube[11] = cValue[53]
    curCube[14] = cValue[52]
    curCube[17] = cValue[51]
    #under
    curCube[51] = cValue[27]
    curCube[52] = cValue[30]
    curCube[53] = cValue[33]
    #left
    curCube[27] = cValue[38]
    curCube[30] = cValue[37]
    curCube[33] = cValue[36]
    finCube = "".join(curCube)
    return finCube


def facesB(cValue):
    curCube = list(cValue)
    #front
    curCube[18] = cValue[20]
    curCube[19] = cValue[23]
    curCube[20] = cValue[26]
    curCube[21] = cValue[19]
#    curCube[22] = cValue[19]
    curCube[23] = cValue[25]
    curCube[24] = cValue[18]
    curCube[25] = cValue[21]
    curCube[26] = cValue[24]
    #top
    curCube[36] = cValue[33]
    curCube[37] = cValue[30]
    curCube[38] = cValue[27]
    #right
    curCube[11] = cValue[36]
    curCube[14] = cValue[37]
    curCube[17] = cValue[38]
    #under
    curCube[51] = cValue[17]
    curCube[52] = cValue[14]
    curCube[53] = cValue[11]
    #left
    curCube[27] = cValue[51]
    curCube[30] = cValue[52]
    curCube[33] = cValue[53]
    finCube = "".join(curCube)
    return finCube

def facesr(cValue):
    curCube = list(cValue)
    #250 front
    curCube[9] = cValue[15]
    curCube[10] = cValue[12]
    curCube[11] = cValue[9]
    curCube[12] = cValue[16]
#    curCube[13] = cValue[19]
    curCube[14] = cValue[10]
    curCube[15] = cValue[17]
    curCube[16] = cValue[14]
    curCube[17] = cValue[11]
    #top
    curCube[44] = cValue[8]
    curCube[41] = cValue[5]
    curCube[38] = cValue[2]
    #right
    curCube[18] = cValue[44]
    curCube[21] = cValue[41]
    curCube[24] = cValue[38]
    #under
    curCube[47] = cValue[24]
    curCube[50] = cValue[21]
    curCube[53] = cValue[18]
    #left
    curCube[2] = cValue[47]
    curCube[5] = cValue[50]
    curCube[8] = cValue[53]
    finCube = "".join(curCube)
    return finCube

def facesR(cValue):
    curCube = list(cValue)
    #front
    curCube[9] = cValue[11]
    curCube[10] = cValue[14]
    curCube[11] = cValue[17]
    curCube[12] = cValue[10]
#    curCube[13] = cValue[19]
    curCube[14] = cValue[16]
    curCube[15] = cValue[9]
    curCube[16] = cValue[12]
    curCube[17] = cValue[15]
    #top
    curCube[44] = cValue[18]
    curCube[41] = cValue[21]
    curCube[38] = cValue[24]
    #right
    curCube[18] = cValue[53]
    curCube[21] = cValue[50]
    curCube[24] = cValue[47]
    #under
    curCube[47] = cValue[2]
    curCube[50] = cValue[5]
    curCube[53] = cValue[8]
    #left
    curCube[2] = cValue[38]
    curCube[5] = cValue[41]
    curCube[8] = cValue[44]
    finCube = "".join(curCube)
    return finCube
#300

def facesl(cValue):
    curCube = list(cValue)
    #front
    curCube[27] = cValue[33]
    curCube[28] = cValue[30]
    curCube[29] = cValue[27]
    curCube[30] = cValue[34]
#    curCube[31] = cValue[19]
    curCube[32] = cValue[28]
    curCube[33] = cValue[35]
    curCube[34] = cValue[32]
    curCube[35] = cValue[29]
    #top
    curCube[42] = cValue[20]
    curCube[39] = cValue[23]
    curCube[36] = cValue[26]
    #right
    curCube[20] = cValue[51]
    curCube[23] = cValue[48]
    curCube[26] = cValue[45]
    #under
    curCube[45] = cValue[0]
    curCube[48] = cValue[3]
    curCube[51] = cValue[6]
    #left
    curCube[0] = cValue[36]
    curCube[3] = cValue[39]
    curCube[6] = cValue[42]
    finCube = "".join(curCube)
    return finCube

def facesL(cValue):
    curCube = list(cValue)
    #front
    curCube[27] = cValue[29]
    curCube[28] = cValue[32]
    curCube[29] = cValue[35]
    curCube[30] = cValue[28]
#    curCube[31] = cValue[19]
    curCube[32] = cValue[34]
    curCube[33] = cValue[27]
    curCube[34] = cValue[30]
    curCube[35] = cValue[33]
    #top
    curCube[42] = cValue[6]
    curCube[39] = cValue[3]
    curCube[36] = cValue[0]
    #right
    curCube[20] = cValue[42]
    curCube[23] = cValue[39]
    curCube[26] = cValue[36]
    #under
    curCube[45] = cValue[26]
    curCube[48] = cValue[23]
    curCube[51] = cValue[20]
    #left
    curCube[0] = cValue[45]
    curCube[3] = cValue[48]
    curCube[6] = cValue[51]
    finCube = "".join(curCube)
    return finCube

def facest(cValue):
    curCube = list(cValue)
    
    curCube[36] = cValue[42]
    curCube[37] = cValue[39]
    curCube[38] = cValue[36]
    curCube[39] = cValue[43]
    curCube[41] = cValue[37]
    curCube[42] = cValue[44]
    curCube[43] = cValue[41]
    curCube[44] = cValue[38]

    curCube[27] = cValue[0]
    curCube[28] = cValue[1]
    curCube[29] = cValue[2]

    curCube[9] = cValue[18]
    curCube[10] = cValue[19]
    curCube[11] = cValue[20]

    curCube[18] = cValue[27]
    curCube[19] = cValue[28]
    curCube[20] = cValue[29]

    curCube[0] = cValue[9]
    curCube[1] = cValue[10]
    curCube[2] = cValue[11]
    finCube = "".join(curCube)
    return finCube

def facesT(cValue):
    curCube = list(cValue)
    
    curCube[36] = cValue[38]
    curCube[37] = cValue[41]
    curCube[38] = cValue[44]
    curCube[39] = cValue[37]
    curCube[41] = cValue[43]
    curCube[42] = cValue[36]
    curCube[43] = cValue[39]
    curCube[44] = cValue[42]

    curCube[27] = cValue[18]
    curCube[28] = cValue[19]
    curCube[29] = cValue[20]

    curCube[9] = cValue[0]
    curCube[10] = cValue[1]
    curCube[11] = cValue[2]

    curCube[18] = cValue[9]
    curCube[19] = cValue[10]
    curCube[20] = cValue[11]

    curCube[0] = cValue[27]
    curCube[1] = cValue[28]
    curCube[2] = cValue[29]
    finCube = "".join(curCube)
    return finCube

def facesu(cValue):
    curCube = list(cValue)
    
    curCube[45] = cValue[51]
#400
    curCube[46] = cValue[48]
    curCube[47] = cValue[45]
    curCube[48] = cValue[52]
    curCube[50] = cValue[46]
    curCube[51] = cValue[53]
    curCube[52] = cValue[50]
    curCube[53] = cValue[47]

    curCube[33] = cValue[24]
    curCube[34] = cValue[25]
    curCube[35] = cValue[26]

    curCube[24] = cValue[15]
    curCube[25] = cValue[16]
    curCube[26] = cValue[17]

    curCube[15] = cValue[6]
    curCube[16] = cValue[7]
    curCube[17] = cValue[8]

    curCube[6] = cValue[33]
    curCube[7] = cValue[34]
    curCube[8] = cValue[35]
    finCube = "".join(curCube)
    return finCube

def facesU(cValue):
    curCube = list(cValue)
    
    curCube[45] = cValue[47]
    curCube[46] = cValue[50]
    curCube[47] = cValue[53]
    curCube[48] = cValue[46]
    curCube[50] = cValue[52]
    curCube[51] = cValue[45]
    curCube[52] = cValue[48]
    curCube[53] = cValue[51]

    curCube[33] = cValue[6]
    curCube[34] = cValue[7]
    curCube[35] = cValue[8]

    curCube[24] = cValue[33]
    curCube[25] = cValue[34]
    curCube[26] = cValue[35]

    curCube[15] = cValue[24]
    curCube[16] = cValue[25]
    curCube[17] = cValue[26]

    curCube[6] = cValue[15]
    curCube[7] = cValue[16]
    curCube[8] = cValue[17]
    finCube = "".join(curCube)
    return finCube


def integrity(x):
    integrity = hashlib.sha256(x.encode('utf-8')).hexdigest().upper()                
    return integrity
    
#449 loc





    
    

