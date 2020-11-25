number=input("enter num:")#2
i=1
sum=0
while(i<=int(number)):#1<=2 2<=2
    data=number*i#data="2"*1="2" #"2"*2="22"
    sum=sum+int(data)#0+2=2 2+int("22")=24
    i+=1#2
print(sum)