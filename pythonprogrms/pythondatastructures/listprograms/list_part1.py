#define by using []
lst=[]
print(type(lst))

#list function
lst=["java","pyhton","c#","javasript"]
#       0       1      2        3
print(lst[0:4])#in order

#slicing
print(lst[0])
print(lst[3])
print(lst[-1])
print(lst[-2])
print(lst[-1:-4:-1])
print(lst[4:0])
print(lst[-1:-5:-1])#reverse
print(lst[0:4:2])
print(lst[:3])
#to add a new element into the list
lst.append("dart")
#replacing java by ruby
lst[0]="ruby"
print(lst)
#inserting an object into a specific position
lst.insert(3,"perl")
print(lst)
#one by one iteration
for item in lst:
    print("item",item)


