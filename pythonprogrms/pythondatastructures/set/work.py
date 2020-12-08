names=["a","b","c","e","f"]

passed=["a","b","c"]
#convert to set and and find the no of failed

st=set(names)
print("names",st)
st2=set(passed)
print("passed",st2)
print ("failed",st.difference(st2))
#OR
failed=st-st2
print(failed)