def q5():
    def isPangram(s:str):
        set1=set(s.lower())
        alphast='qwertyuiopasdfghjklzxcvbnm'
        alphaset=set(alphast)
        for s in alphaset:
            if set(s) <= set1:
                pass
            else:
                return False
        return True
    ans1=isPangram("The quick brown fox jumps over the lazy dog")
    ans2=isPangram("Crazy Fredrick bought many very exquisite opal jewels")
    print(ans1,ans2)
q5()
