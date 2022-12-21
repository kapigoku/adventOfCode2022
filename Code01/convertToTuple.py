def convertToTuple():
    openFile = open('test01.txt','r')
    textFile = openFile.read().splitlines()
    
    newList=list()
    temp=list()
    for i in textFile:
        if(i == ''):
            newList.append(temp)
            temp=list()
        else:
            temp.append(int(i))
    
    return tuple(map(tuple,newList))