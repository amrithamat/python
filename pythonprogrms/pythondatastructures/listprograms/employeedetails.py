employees=[[1001,"ajay","qa",1981,2003],
           [1002,"vijay","developer",1992,2008],
           [1003,"arun","ba",1989,2010],
           [1002,"amal","developer",2009,2014],
           [1004,"vimal","developer",1987,1989]]
#print all employee designation
for employee in employees:
    print(employee[2])


#print all employee whose desi=developer
for employee in employees:
    if employee[2]=='developer':
        print(employee)

#print all employee who are working in 1980s
for employee in employees:
    if employee[3]<1999:
        if employee[3]>1979:
            print(employee[1])

#print all employee details whose experinece>9yrs
for employee in employees:
    if((employee[4]-employee[3])>9):
        print(employee)