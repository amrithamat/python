#stack operation
stack=[]
stack.append('a')
stack.append('b')
stack.append('c')
print("initial stack",stack)
top=-1
if(top>2):
    print("stack is full")

else:
    stack[top]=10
    top+=1

print(stack)