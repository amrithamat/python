text="hello hai hai hello hai"
#o/p: hello:2 hai:3
words=text.split(" ")
print(words)
result=len(words)
print("word length=",result)
dict={}
#need to store hai n hai to dict
#{hello:1,hai:1} then incerement it
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
