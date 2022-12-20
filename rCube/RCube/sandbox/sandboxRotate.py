'''
Created on Nov 30, 2020

@author: chrisflodstrom
'''

import hashlib

def _sandbox(parms):
    cubeContent = parms['cube']

    integrityHash = hashlib.sha256(cubeContent.encode()).hexdigest().upper()
    return {'cube': cubeContent, 'integrity': integrityHash}