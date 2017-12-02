def AddAround(listIn):
    strList = str(listIn)
    listLength = len(strList)
    spacing = int(listLength/2)

    return sum([int(num) for (i,num) in enumerate(strList) if strList[i] == strList[(i+spacing)%listLength]])
