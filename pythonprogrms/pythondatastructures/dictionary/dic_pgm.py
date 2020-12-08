#values stored as key value pair

#students=[100,"ajay","bca"]
students={"rol":100,"name":"ajay","course":"bca"}
#print student name ajay
#ajay is a value to fetch value we have to use corresponding key
print(students["name"])
#print course
print(students["course"])
#to iterate values
for item in students:
    print(item)#rol,name,course
for key in students:
    print(key,students[key])

for k,v in students.items():
    print(k,v)

#checking for a key eg:rolno
print("rol" in students) #true
print("total" in students)#false
#checking for total key ie;adding new key value pair
if("total" not in students):
    students["total"]=150
    print(students)

#adding 50 to already existing total
students["total"]+=50
print(students)

#error : unhashable type: 'dict'
"""student={{"rol":100,"name":"ajay","course":"bca"},
        {"rol":101,"name":"vijay","course":"mca"}}
print(student)"""
#error corrected
student={100:{"rol":100,"name":"ajay","course":"bca"},
         101:{"rol":101,"name":"vijay","course":"mca"}}
print(student)

#python dict, java-->hasgmap(),javasript-->object, c-->struct, union



