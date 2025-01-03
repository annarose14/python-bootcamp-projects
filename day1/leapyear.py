def is_leap_year(year):
    result=True
    if(year%4 ==0 and year%100 !=0):
        return True
    elif year%400 ==0:
        return True
    else:
        return False
x=is_leap_year(2024)
print(x)
        