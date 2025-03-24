def q8():
    def convert(st:str):
        words = set(st.split())  
        sorted_words = sorted(words)  
        return " ".join(sorted_words)  


    string = "yug 6 ronit 1 rudresh 5 tanmesh 8 krish 69"
    print(convert(string)) 
q8() 
