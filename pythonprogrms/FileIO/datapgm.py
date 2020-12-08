f=open("data","r")
lst=[]
st=set(lst)
for lines in f:
    st.add(lines.rstrip("\n"))
print(st)

#or
f=open("data","r")
st=set()
for lines in f:
    st.add(lines.rstrip("\n"))
print(st)

