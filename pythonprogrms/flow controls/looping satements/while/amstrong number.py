#cube of num ... ie...armstrong number

number=int(input("enter the number"))
result=0
while(number!=0):
    digit=number%10
    result=result+(digit**3)
    number=number//10
print(result)