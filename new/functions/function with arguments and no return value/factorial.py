number=int(input("enter value"))
def fact(number):
    fact = 1
    for i in range(1,(number+1)):
        fact*=i
    print("factorial of ",number,"is",fact)
fact(number)