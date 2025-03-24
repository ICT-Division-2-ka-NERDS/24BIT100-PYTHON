def q4():
    st=input("Enter any string")
    d={}
    for i in st:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)