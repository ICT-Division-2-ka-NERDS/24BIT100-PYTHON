def q11():
    def create_list(l1:list,l2:list):
        l=[]
        for i in l1:
            if(i in l2):
                l.append(i)
            else:
                continue
        return l
    lst=create_list([1,2,3,4,5,6,7,8,9,0],[2,66,9,11,4,22,0])
    print(lst)
q11()