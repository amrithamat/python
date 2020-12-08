f=open("complete.csv")
dict={}
for lines in f:
    print(lines)
    data=lines.rstrip("\n").split(",")
    print(data)
    state=data[1]
    confirmed_cases=int(data[4])
    if state not in dict:
        dict[state]=int(confirmed_cases)
    else:
        dict[state]=int(confirmed_cases)

for k,v in dict.items():
    print(k,v)
#find state which have highest confirmed cases
highest=max(dict,key=dict.get)#.get used to get the value, key is an argument no connecteion wid dict
print("highest=",highest,dict[highest])
#find state which have lowest confirmd cases
lowest=min(dict,key=dict.get)
print("lowest=",lowest,dict[lowest])
#sort the state depend on cofirmed cases
srt=sorted(dict,key=dict.get,reverse=True)
print("sorted order=",srt)
