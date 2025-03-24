def q12():
    radius=float(input("Enter the value of radius"))
    x=float(input("Enter the x coordinate of centre of circle"))
    y=float(input("Enter the y coordinate of centre of circle"))
    x1=float(input("Enter the x coordinate of the point you want to check"))
    y1=float(input("Enter the y coordinate of the point you want to check"))
    func=(x-x1)**2+(y-y1)**2-radius**2
    print("The given point lies inside the circle") if(func<0) else print("The given point doesn't lies inside the circle")
