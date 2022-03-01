def chop(xList):
    xList.remove(xList[len(xList)-1])
    xList.remove(xList[0])
    print(xList)
    return None

