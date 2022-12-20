"""
Chris Flodstrom
czf0038
Assignment 07-01

https://www.w3schools.com/python/ref_list_append.asp
https://www.w3schools.com/python/python_lists.asp


"""
import hashlib

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

def integrityCheck(face, integ):
    hashl = hashlib.sha256(face.encode()).hexdigest().upper()
    if hashl == integ:
        return True 
    else:
        return False 
    
    
def spotChecker(faces):
    for j in range(6):
        val = j * 9
        if  not (faces[val] is faces[val + 1] and faces[val] is faces[val + 2] and faces[val] is faces[val + 3] and faces[val] is faces[val + 5] \
                 and faces[val] is faces[val + 6] and faces[val] is faces[val + 7] and faces[val] is faces[val + 8]):
            return False
        if faces[val] is faces[val + 4]:
            return False
    return True   

def crossChecker(faces):
    for j in range(6):
        val = j * 9
        if not (faces[val] is faces[val + 2] and faces[val] is faces[val + 6] and faces[val] is faces[val + 8]):
            return False
        if not (faces[val + 1] is faces[val + 3] and faces[val + 1] is faces[val + 4] and faces[val + 1] is faces[val + 5] and faces[val + 1] is faces[val + 7]):
            return False
    return True

def _check(parms):
    result = {}

    if not 'cube' in parms:
        return {'status': 'error: missing cube parameters'}

    elif len(parms['cube']) == 0:
        return {'status': 'error: Cube is empty'}

    elif not 'integrity' in parms:
        return {'status': 'error: Cube does not have integrity key'}

    elif len(parms['integrity']) == 0:
        return {'status': 'error: does not have integrity value'}

    elif not integrityCheck(parms['cube'], parms['integrity']):
        return {'status': 'error: does not match integrity value'}

    elif len(parms['cube']) != 54:
        return {'status': 'error: Incorrect number of elements, needs to be 54'}

    elif not sixElements(parms['cube']):
        return {'status': 'error: needs 6 unique elements'}

    elif not colorChecker(parms['cube']):
        return {'status': 'error: needs 9 colors'}

    elif not checkMiddle(parms['cube']):
        return {'status': 'error: needs distinct middle numbers'}
# 
    elif not checkCorner(parms['cube']):
        return {'status': 'error: impossible corner'}
 
    elif not checkEdges(parms['cube']):
        return {'status': 'error: impossible edge'}
    
    elif checkIfFull(parms['cube']):
        return {'status': 'full'}
    
    elif spotChecker(parms['cube']):
        return {'status': 'spots'}
 
    elif crossChecker(parms['cube']):
        return {'status': 'crosses'}# 
    else:
        return {'status': 'unknown'}
        
def checkMiddle(faces):
    typeColor = []
    for j in range(6):
        val = j * 9
        if faces[val + 4] in typeColor:
            return False
        else:
            typeColor.append(faces[val + 4]) 
    return True 

def checkIfFull(faces):
    for j in range(6):
        val = j * 9
        for j in range(1, 9):
            if not faces[val] is faces[val + j]:
                return False
    return True
# 
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
