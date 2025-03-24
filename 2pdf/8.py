def q8():
    angle1=int(input("Enter the first angle of triangle"))
    angle2=int(input("Enter the second angle of triangle"))
    angle3=int(input("Enter the third angle of triangle"))
    print("The triangle is valid")if(angle1+angle2+angle3==180) else print("The triangle is not valid")