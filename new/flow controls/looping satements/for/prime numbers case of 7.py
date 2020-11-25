#prime number 1,number will be the factor
#eg: 7---->1,7 prime
#implement in 7
#exclude 1 and 7
flag=0
for i in range(2,7):
    if(7%i==0):#7%2==0
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

