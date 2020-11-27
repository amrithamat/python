lst=[120,11,12,13,14]#seaching for an element
flag=0
element=int(input("enter the search element"))
for i in lst:
    if(i==element):
        flag=1# or flag+=1
        break
    else:
        flag=0
if(flag==1):# or flag>0
    print("search found")
else:
    print("not found")

#algorithm used: linear