def q4():
    def sum_avg(**arg):
        total=0
        for v in arg:
            total=total+v
        avg=total/5
        return total,avg
    total,avg=sum_avg(100,100,100,100,100)
