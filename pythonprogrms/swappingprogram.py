#using a temp
num1=10
num2=20
print("values b4 swapping num1=",num1,"num2=",num2)
temp=num1
num1=num2
num2=temp
print("values after swapping num1=",num1,"num2=",num2)

#without using temp value
num3=10
num4=20
print("values b4 swapping num3=",num3,"num4=",num4)
num3=num3+num4
num4=num3-num4
num3=num3-num4
print("values after swapping num3=",num3,"num4=",num4)

#method only using in python for swapping
num5=10
num6=20
print("values b4 swapping num5=",num5,"num6=",num6)
(num5,num6)=(num6,num5)
print("values after swapping num5=",num5,"num6=",num6)

#input passing
num7=input("enter the value for num7")
num8=input("enter the vlaue for num8")
print("values b4 swapping num7=",num7,"num8=",num8)
(num7,num8)=(num8,num7)
print("values after swapping num7=",num7,"num8=",num8)