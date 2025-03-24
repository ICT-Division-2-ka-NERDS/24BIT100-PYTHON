def q9():
    def count_alpha_digits(st:str):
        alphabets=list(st)
        numCount=0
        alphaCount=0
        for i in alphabets:
            if i.isnumeric():
                numCount+=1
            elif i.isalpha():
                alphaCount+=1
            else:
                pass
        return {"Digit":numCount,"Alphabets":alphaCount}
    st_count=count_alpha_digits("yug 6 ronit 1 rudresh 5 tanmesh 8 krish 69")
    print(st_count)
q9()