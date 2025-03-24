import random
def q2():
    lst=[]
    for i in range(20):
        lst.append(random.randint(1,10))
    print(lst)
    inp=int(input("Enter the number whose occurence is required between 1-9:"))
    for j in range(10):
        if lst[j]==inp:
            print(j)
