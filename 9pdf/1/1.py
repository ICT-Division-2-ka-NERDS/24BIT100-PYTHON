def q1():
    def count_lower_upper(string:str):
        upperCase=0
        lowerCase=0
        for i in string:
            if (i.isupper()):
                upperCase+=1
            elif(i.islower()):
                lowerCase+=1
            else:
                pass
        return {"UpperCase":upperCase,"LowerCase":lowerCase}
    s1="My Name iS RoniT"
    print(count_lower_upper(s1))
q1()