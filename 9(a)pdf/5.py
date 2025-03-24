def q5():
    def filterFaculty(faculty:list):
        return list(filter(lambda x: True if len(x)>8 else False,faculty))
    print(filterFaculty(["FVA J","JHQAFVC","GYUKVDCQA","GYYLwcblwlcja"]))
q5()