low=int(input("enter the lowerlimit:"))#2
upp=int(input("enter the upperlimit:"))#16
sum=0
if(low>upp):
    print("error")
while(low<=upp):
    if(low%2!=0):
        sum+=low
    low+=1
print("sum=",sum)


