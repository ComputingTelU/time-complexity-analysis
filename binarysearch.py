def binarysearch(array, x):
    minind = 0
    maxind = len(array)
    currind = 0
    currelm = 0

    while(minind <= maxind):
        currind = (minind+maxind)/2
        currelm = array[currind]

        if(currelm < x):
            minind = currind + 1
        elif(currelm > x):
            maxind = currind - 1
        else:
            return currind
        
        print(minind, maxind)

    return -1