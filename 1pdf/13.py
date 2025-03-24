def q13():
    byte=int(input("Enter the no of bytes you want to covert"))
    Kb=byte/1024
    Mb=Kb/1024
    Gb=Mb/1024
    print("The bytes in Kb,Mb and Gb are",Kb,Mb,Gb,"respectively",sep=",")
