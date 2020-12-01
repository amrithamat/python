employees=[[1001,"ajay","qa",15000],
           [1002,"vijay","developer",25000],
           [1003,"arum","ba",15000],
           [1004,"amal","developer",30000]]
#print all employee id
for employee in employees:
    print(employee[0])

#Find total of salary
totalsal=0
for employee in employees:
    totalsal+=employee[3]
print(totalsal)


#find how many members working as developer
for employee in employees:
    if employee[2]=='developer':
        print(employee)

#find total of salary group by designation
totalqa=0
totaldev=0
for employee in employees:
    if(employee[2]=="qa"):
        totalqa+=employee[3]
    if(employee[2]=="developer"):
        totaldev+=employee[3]
print("qa total salry",totalqa)
print("developer total salry",totaldev)