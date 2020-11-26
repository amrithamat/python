lst=[1,2,3,4,5,6,7]
#value=6 (4,2)
sum=6
for i in lst:
    for j in lst:
        sumtotal=i+j
        if(sum==sumtotal):
            print((i,j))
            break
#more running time
#not efficient