import datetime
print(datetime.datetime.today())#currentdate



bdaydate=input("enter your bday dd-mm-yyyy:")
currentdate=input("enter current date dd-mm-yyyy:")


print(bdaydate)#20-11-2019
print(currentdate)#18-11-2020

bdate,bmonth,byear=bdaydate.split("-")#20-11-2019
cdate,cmonth,cyear=currentdate.split("-")#18-11-2020
age=int(cyear)-int(byear)#age=1
print(age)
if(cmonth>=bmonth):#11<=11
    if(cdate<bdate):#18<20
        age-=1#age=0
print("ypu are",age,"years old")

