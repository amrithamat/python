#2
#2+22=24
#3
#3+33+333=369
#4
#4+44+444+4444=


number = int(input("enter the num:"))
i=0
sum=0
p=0
while(i<number):
    p=p+((10**i)*number)
    sum+=p
    i+=1
print(sum)
