def q3():
    string=input("Enter any string:")
    Ncount,Acount=0,0
    for ch in string:
        if ch.isalpha():
            Acount+=1
        elif ch.isnumeric():
            Ncount+=1
        else:
            pass
    print("The No of alphabets in string is",Acount)
    print("The No of digits in string is",Ncount)

