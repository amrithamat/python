lst=[12,2,34,5,77,51]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]<lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)