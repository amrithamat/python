names=["a","b","c","e","f"]

passed=["a","b","c"]
#convert to set and and find the no of failed

st=set(names)
print(st)
st2=set(passed)
print(st2)
failed=(st.difference(st2))
print (failed)
