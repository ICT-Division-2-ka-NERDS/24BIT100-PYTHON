def q5():
    l=[(),'Ronit',('lst',),[1,2,3],[]]
    for i in l:
        if(type(i)==tuple and len(i)==0):
            l.remove(i)
        else:
            pass
    print(l)