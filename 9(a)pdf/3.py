import random
def q3():
    l=[random.randint(-15,15) for i in range(10)]
    sq_l=list(map(lambda x:x*x,l))
    print(sq_l)
q3()