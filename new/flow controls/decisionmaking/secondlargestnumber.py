num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if((num1>num2)^(num1>num3)):
    print("second largest number is",num1)
elif((num2>num1)^(num2>num3)):
    print("second largest number is",num2)
elif((num3>num1)^(num3>num2)):
    print("second largest number is",num3)
else:
    print("numbers are equal")

