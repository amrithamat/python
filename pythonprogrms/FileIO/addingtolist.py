

"""data="hello\n"
data=data.rstrip("\n")#remove from right
data="\nhello"
data=data.lstrip("\n")#remove from left"""

f=open("names","r")
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
print(lst)