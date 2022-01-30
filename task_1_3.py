number = 0
while number < 100:
    number += 1
    if number % 10 == 0 or 5 <= number % 10 <= 9 or number == 11 or number == 12 or number == 13 or number == 14:
        declination = 'Процентов'
    elif number % 10 == 1:
        declination = 'Процент'
    elif 2 <= number % 10 <= 4:
        declination = 'Процента'
    print(number, declination)