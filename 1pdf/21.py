def q21():
    gross_salary=float(input("Enter the gross salary"))
    allowance=0.1*gross_salary
    deduction=0.03*gross_salary
    NetSalary=gross_salary + allowance - deduction
    print("The Net salary is ",NetSalary)
