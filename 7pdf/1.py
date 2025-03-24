def q1():
    d={}
    d0={"brand": "Ford","model": "Mustang","year": 1964}
    d1={'type' : 'fruit', 'name' : 'banana'}
    d2={"Germany": "Berlin", "Canada": "Ottawa", "England": "London"}
    d.update(d0)
    d.update(d1)
    d.update(d2)
    print(d)