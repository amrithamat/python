lst=[10,9,8,11,12,5,6]#find second largest number
#also print ascending and descending order

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]<lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)
print(lst[1],"second largest")