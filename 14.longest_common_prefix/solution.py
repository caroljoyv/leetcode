strs = ["ab", "a"]

## solution 1

def find(strs):
    prefix = ""

    #find the smallest word
    smallest = strs[0]
    for i in range(1,len(strs)):
        if len(strs[i]) < len(smallest):
            smallest = strs[i]    

    for i in range(len(smallest)): # loop iterates through all characters of the first wrd
        for j in strs: # loop iterated through all words in strs
            if smallest[i] != j[i] or len(j) == i :
                return prefix
        prefix += smallest[i]
    return prefix

print(find(strs))


## solution 2

def find2(strs):
     
    #find the smallest word
    smallest = strs[0]
    for i in range(1,len(strs)):
        if len(strs[i]) < len(smallest):
            smallest = strs[i] 

    prefix = smallest

    for s in strs:
        iP, iS = 0, 0 # index of prefix, index of current string
        while iP < len(prefix) and iS < len(s): # make sure neither index is out of bounds
            if prefix[iP] == s[iS]: # match? simply increment both indices
                iP+=1
                iS+=1
            else: # first mismatch
                prefix = prefix[0:iP] # set prefix to the shorter of two
                iP = len(prefix) # exit while loop
    return prefix

print(find2(strs))
