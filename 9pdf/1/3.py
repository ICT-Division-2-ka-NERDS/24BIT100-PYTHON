def q3():
    def create_array(size1:int,size2:int,size3:int,value:int):
        l=[[ [value for k in range(size3)]for j in range(size2)] for i in range(size1)]
        return l
    lst=create_array(3,4,5,1)
    print(lst)
q3()
