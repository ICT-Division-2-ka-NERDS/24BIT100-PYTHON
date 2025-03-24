def q1():
    count=0
    string=input("Enter any string")
    for char in string:
        if(char in "aeiouAEIOU"):
            count+=1
        else:
            pass
    print("The No of vowels in the given string is",count)
    