students={
        100:{"rol":100,"name":"ajay","total":140,"course":"bca"},
        101: {"rol": 101, "name":"vijay", "total":143, "course": "bca"},
        102: {"rol": 102, "name":"anu", "total":148, "course": "bca"},
        103: {"rol": 103, "name":"arya", "total":145, "course": "bca"},
        104: {"rol": 104, "name":"sera", "total":149, "course": "bca"}
}
print(students[100])
print(students[100]["name"])
print(students[100]["total"])

def printStudent(**kwargs):#kwargs recieve in the formar {id:101}
    #print(kwargs)
    id=kwargs.get("id")#100 id=kwargs["id"] 101
    if(id in students):#check this id in dict
        if "property" in kwargs:# check whether property is there or not
            prop=kwargs.get("propert")
            if prop in students[id]:
                print(students[id][prop])#if there is id print the name
        print(students[id]["name"])
    else:
        print("student with this rol not exist")
printStudent(id=100)
printStudent(id=109)
printStudent(id=104,property="total")#property is fixed we can change the value in that