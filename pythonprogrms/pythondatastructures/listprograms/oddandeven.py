#store odd and even numbers into separte list
lst=[20,40,30,55,60,77]
even=[]
odd=[]
for num in lst:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(odd)
print(even)

