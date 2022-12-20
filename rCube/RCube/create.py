import hashlib
"""
Chris Flodstrom
czf0038
Assignment 04-01
"""

def _create(parms):
    result = {'cube':'', 'integrity':'', 'status':''}
    rCubeStr = ''
    faces = 'faces'
    

    if 'faces' not in parms:
        parms['faces'] = 'gybwro'
                   
    if 'faces' in parms:
        something = parms['faces']
        for value in something:
            if something.count(value) > 1:
                return {'status':'error: There is a duplicate number'}
                  
        if parms['faces'] == '':
                    parms['faces'] = 'gybwro'        
        
        if(len(something) != 6 and len(something) > 0):
                    return{'status':'error: There is an invalid length of faces'} 

    for color in parms['faces']:
        for i in range (9):
            rCubeStr += color
            
    result['cube'] = rCubeStr    

    integrity = hashlib.sha256(rCubeStr.encode('utf-8')).hexdigest().upper()
    result['integrity'] = integrity
    
    cubeSomething = {'cube': rCubeStr, 'integrity': integrity, 'status': 'ok'}
    return cubeSomething
