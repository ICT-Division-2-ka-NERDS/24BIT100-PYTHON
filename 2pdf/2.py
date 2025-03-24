def q2():
    n1=int(input("First Number:"))
    n2=int(input("Second Number:"))
    n3=int(input("Third Number:"))
    
    if(n1>n2):
        if(n2>n3):
            print(n1,"is larger and",n3,"is smaller value") 
        else:
            print(n1,"is larger and",n2,"is smaller value") 
    elif(n1>n3):
        print(n2,"is larger and",n3,"is smaller value") 
    else:
        if(n2>n3):
            print(n2,"is larger and",n1,"is smaller value")
        else:
            print(n3,"is larger and",n1,"is smaller value")
q2()
