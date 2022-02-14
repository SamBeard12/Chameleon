import warnings

initial = ['cat', 'dog', 'monkey', 'lion', 'fish', 'aardvark']

before = ['dog']

after = ['cat']

def ConstrainedInsert(initial, item, after, before):
    """This function takes an initial array and inserts 'item' into
    a position that is after every element in 'before' and before all the
    elements in 'after', or raising an error if the constraints are not
    solvable """
    #Find indicies of items in the before array
    beforeInd = []
    for element in before:
        #Finds first index for each element in before in initial
        try:
            beforeInd.append(initial.index(element))
        #UserWarning if string in after is not in initial
        except:
            warnings.warn('{} is not in initial'.format(element))

    #Find indicies of items in the after array
    afterInd = []
    for element in after:
        #Finds last index for each element in after in initial (reversed in case of repeaded elements in initial)
        try:
            afterInd.append(len(initial)-initial[::-1].index(element)-1)
        #UserWarning if string in after is not in initial
        except:
            warnings.warn('{} is not in initial'.format(element))
    
    if len(afterInd) > 0 and len(beforeInd)>0:
        if max(afterInd)<min(beforeInd):
            #Inserts item into array after last element in after if solvable constraints
            initial.insert((max(afterInd)+1), item)
        else:
            #Raises ValueError if constraints arent solvable
            raise ValueError('Constraints not solvable')
    elif len(afterInd) == 0 and len(beforeInd) > 0:
        initial.insert(min(beforeInd), item)
    else:
        initial.insert(max(afterInd)+1, item)

    return initial

print(ConstrainedInsert(initial, 'orca', after, before))



    
    
        
