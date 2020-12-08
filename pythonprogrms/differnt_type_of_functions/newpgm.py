"""def add(num1,num2):
    res=num1+num2
    print(res)
add(10,20)"""

#variable length arguments method

"""def add(*nums):
    print(nums)
add(10,20)
add(10,20,30,40)
add(10,11,12,13,14)"""

def add(*args):
    total=0
    for num in args:
        total+=num
    print(total)
add(10,20)
add(10,20,30,40)
add(10,11,12,13,14)


def printEmp(*args):#*args accepted as tuple
    print(args)
printEmp("kakkanad","ajay","aluva")

def printEmp(**args):#**args accepted as dict ie, key value pairs
    print(args)
printEmp(home="kakkanad",name="ajay",working="aluva")