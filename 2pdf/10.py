def q10():
    length=float(input("Enter the length of rectangle"))
    breadth=float(input("Enter the breadth of rectangle"))
    area=length*breadth
    perimeter=2*(length+breadth)
    print("Area is greater than perimeter") if(area>perimeter) else print("Perimeter is greater than area")