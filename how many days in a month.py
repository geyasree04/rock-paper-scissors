import calendar
year=int(input("enter the year:"))
month=int(input("enter the month:"))
flag=False
if year%4==0:
    if year%100==0:
        if year%400==0:
            falg=True
            print(f"the given year {year} is a leap year")
        else:
            flag=False
            print(f"the given year {year} is not a leap year")
    else:
        flag=True
        print(f"the given year {year} is a leap year")
else:
    flag=False
    print(f"the given year {year} is not a leap year")
if month in (1,3,5,7,8,10,12):
    print(f"the month {month} has 31 days....")
elif month in (4,6,9,11):
    print(f"the month {month} has 30 days....")
elif month==2:
    if flag == True:
        print(f"the month {month} has 29 days....")
    else:
        print(f"the month {month} has 28 days....")
        
res=calendar.month(year,month)
print(res)