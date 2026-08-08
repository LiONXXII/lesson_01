def is_leap_year(year):         # високосный ли год?
    if year % 400 == 0:         # если остаток от деления на 400 равен нулю
        return True
    if year % 100 == 0:         # если остаток от деления на 100 равен нулю
        return False
    if year % 4 == 0:           # если остаток от деления на 4 равен нулю
        return True
    return False


year = 2024
result = is_leap_year(year)
print(f"год {year}: {result}")
