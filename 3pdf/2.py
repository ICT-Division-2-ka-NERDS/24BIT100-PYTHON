def q2():
    def upperCase():
        output=''
        dummy=0
        string=input("Enter any string:")
        for char in string:
            if 'z'>=char>='a':
                dummy=ord(char)
                dummy=dummy-32
                c=chr(dummy)
                output=output+c
            else:
                output=output+char
        print(output)


    def lowercase():
        output=''
        dummy=0
        string=input("Enter any string:")
        for char in string:
            if 'A'<=char<='Z':
                dummy=ord(char)
                dummy=dummy+32
                c=chr(dummy)
                output=output+c
            else:
                output=output+char
        print(output)
    

    def toggleCase():
        output=''
        dummy=0
        string=input("Enter any string:")
        for char in string:
            if 'A'<=char<='Z':
                dummy=ord(char)
                dummy=dummy+32
                c=chr(dummy)
                output=output+c
            elif 'z'>=char>='a':
                dummy=ord(char)
                dummy=dummy-32
                c=chr(dummy)
                output=output+c
            else:
                output=output+char
        print(output)
    toggleCase()
    
q2()
             