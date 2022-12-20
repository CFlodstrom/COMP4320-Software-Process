#Chris Flodstrom
#czf0038
#Assignment 1
#used StackOverflow for assistance with checking for integers
#first time writing in python
#consulted with Matthew "Tyler" McGlawn for assistance with my issues

def collapse(value):
    
    cvalue = len(value) #length of the value
    chklist = list(value) 
        
    #ensures the value is not a string, has at least one character and no more than 50
    #if it does, "None" will be returned       
    if type(value) != str or cvalue >= 50 or cvalue == 0:
        return None
    
    #Checks to see if a string represents an int
    else:        
        for intchecker in chklist:
            try:
                int(intchecker)
            except ValueError:
                return None
    

    #if the above passes, the calculation will complete and return the answer
    j = int(value)
    if j > 0:
        value = (j - 1) % 9 + 1
    return str(value) 

    
