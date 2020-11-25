
number=int(input("enter number:"))
flag=0
for i in range(2,number):
    if(number%i==0):
        #it has factor
        flag=1
        break
    else:#flage=0
        #no factor
        flag=0
if(flag==0):
    print("prime number")
else:
    print("not prime number")