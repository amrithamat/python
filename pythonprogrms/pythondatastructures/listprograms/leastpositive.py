lst=[-2,-1,0,1,2,3,4]#1
#after adding 1 then another one is 5
#find least positive missing interger from list


#skip all negative numbers
cnt=1#starting from one
for i in range(0,len(lst)):
    if cnt in lst:#check for one in the list, then check for two....like upto 5
        cnt+=1#2,3
        #pass *
    else:
        print(cnt,"is least positive missing integer")
        break

#pass : simply pass