import operator
def q4():
    l=[('Alloo',100),('Burger',120),('pizza',200)]
    lst=sorted(l,key=operator.itemgetter(1),reverse=True)
    print(lst)
    
    
    