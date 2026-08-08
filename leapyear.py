def is_leap(year):
    if (1900<=year and year<= 10**5):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False
    else:
        return False
year = int(input())
print(is_leap(year))
