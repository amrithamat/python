low=int(input("enter low limit"))
upp=int(input("enter upper limit"))
oddsum=0
evensum=0
for i in range(low,upp):
    if(i%2==0):
        evensum+=i
    else:
        oddsum+=i

print(oddsum,",",evensum)