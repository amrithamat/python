lst=[2,1,3,4,6,7]

lst.sort()
low=0
upp=len(lst)-1
element=int(input("enter element"))
while(low<upp):
    total=lst[low]+lst[upp]
    #case1
    if(element<total):
        upp=upp-1
    #case2
    elif(element>total):
        low=low+1
    #case3
    elif(element==total):
        print("pairs are",lst[low],",",lst[upp])
        break



#[1, 2, 3, 4, 6, 7]
#l                u
#6
#lst[l]+lst[u]==6 (1+7=8)
#if searching elemet<total : move upper backwards
#6<8(l<u)
#lst[l]+lst[u]==6 (1+6=7)
#6<7
#lst[l]+lst[u]==6 (1+4=5)
#6>5 is searching element>total :move lower forward
### lst[l]+lst[u]==6 (2+4=6)
#if total==searching elemet return lst[l],lst[u]