st=set()
print(type(st))
set={10,20,30}
st1={100,200}
print(set)
#print(set[0])---->indexing doesnt support

#set operations
set.update(st1)
print(set)
unionset=set.union(st1)
print(unionset)

intersection=set.intersection(st1)
print(intersection)

set.add(55)
print(set)