lst=[2,5,6,3]#14,11,10,13
#lst=[4,3,2,5] #10,11,12,9
out=[]
total=sum(lst) #16
for num in lst:#5,6,3
    out.append((total-num))#16-2=14,16-5=11,16-6=10,16-3=13

print(out)
