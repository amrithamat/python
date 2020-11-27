
#sorting in ascending order normal method
lst=[2,1,4,7,6,8,9,10]
    #0 1 2 3 4 5 6  7   index values
#step1: sort this array
#without using sorting

for i in range(0,len(lst)):
    for j in range((i+1),len(lst)):
        if(lst[i]>lst[j]): #2>1
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)

#using binary search
#[1, 2, 3, 5, 6, 7, 8, 8, 10, 11]
# 0  1  2  3  4  5  6  7  8    9
#low                          upp
#setting lower and upper
low=0
upp=len(lst)-1

#calc mid
mid=(low+upp)//2
print(mid)#4 is the position of middle elemt

element=10
#10 is compared with the midle elemt 6
#10>lsr[mid] 10>6
#case1 element>lst[mid]
   #lower=mid+1
#case2
#consider the searching elemt is 2
#lst[mid]2<6
#no need to search the balance array need to search only upto 6
#upp=mid-1

#case3:searching elemt =6 ie, middle elemt
#element==lst[mid]
#found