lst=[7,2,3,6,8,1,10]
#step 1 sorted list
lst.sort()
#lst=sorted(lst)#sorted is a function

print(lst)

#searching
element=int(input("enter the element you want to search"))
low=0
upp=len(lst)-1
flag=0
while(low<=upp):
    mid=(low+upp)//2
    #case1
    if(element>lst[mid]):
        low=mid+1
    #case2
    elif(element<lst[mid]):
        upp=mid-1
    #case3
    elif(element==lst[mid]):
        flag=1
        break
if (flag>0):
    print("element found")
else:
    print("element not found")



"""import builtins # or from builtins import sorted
def add(num1,num2):
    print(num1,num2)
add(10,20)"""
