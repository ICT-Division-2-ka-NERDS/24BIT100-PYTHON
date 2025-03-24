def q3():
    s=set()
    for i in range(5):
        name=input("Enter the name you want to add in set:")
        s.add(name)
    oldName=input("Enter the name you want to modify:")
    try:
        s.remove(oldName)
        newName=input("Enter the modified name:")
        s.add(newName)
    except:
        print("Value not found in set")
    name=input("Enter the name you want to delete:")
    s.remove(name)
    name=input("Enter the name you want to delete:")
    s.remove(name)
    print(s)
q3()