def q6():
    def tupleInList(x:int):
        lst=[]
        for i in range(1,x+1):
            lst.append((i,i**2,i**3))
        return lst
    l=tupleInList(7)
    print(l)
q6()