#1 2 3 4
#5 6 7 8
#9 10 11 12
count=1
for i in range(1,13):#i=1,2,3,4
        print(i,end="\t")#print 1 2 3 4
        if(count==4):#c==4 no, 2===4 no, 3==4 no,4===4
            print() #print space when 4==4
            count=1
        else:
            count+=1 #c=2 3 4