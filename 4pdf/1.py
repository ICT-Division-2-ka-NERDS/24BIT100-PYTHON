def q1():
    ch = ord('A')  
    while True:
        if ch == 91:  
            ch += 5
        else:
            print(chr(ch))  
        ch += 1  
        if ch >= ord('z'):  
            break
