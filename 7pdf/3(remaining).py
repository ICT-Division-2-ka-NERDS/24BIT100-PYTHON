def q3():
    employees = {
        1: [101, 5000],
        2: [101, 7000],
        3: [101, 3000],
        4: [102, 6000],
        5: [102, 8000],
        6: [102, 4000],
        7: [103, 9000],
        8: [103, 11000],
        9: [103, 6000],
    }
    dept_salary_stats = {}
    
    for emp_no, emp_info in employees.items():
        dept_no = emp_info[0] 
        salary = emp_info[1]

        if dept_no not in dept_salary_stats:
            dept_salary_stats[dept_no] = [salary, salary]  
        else:
            dept_salary_stats[dept_no][0] = min(dept_salary_stats[dept_no][0], salary)
            dept_salary_stats[dept_no][1] = max(dept_salary_stats[dept_no][1], salary)

    for dept_no, stats in dept_salary_stats.items():
        print(f"Department {dept_no}: Min Salary = {stats[0]}, Max Salary = {stats[1]}")
