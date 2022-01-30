duration = int(input('Введите время в секундах: '))
if 0 <= duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'мин', seconds, 'сек')
elif 3600 <= duration < 86400:
    hours = duration // 3600
    minutes = (duration - hours * 3600) // 60
    seconds = duration % 60
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
elif 86400 <= duration:
    days = duration // 86400
    hours = (duration - days * 86400) // 3600
    minutes = ((duration - days * 86400) - hours * 3600) // 60
    seconds = duration % 60
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
else:
    print('Время не может идти вспять))')

print('Ниже пример со списком --------->')

my_list = [4353453, 456123153, 78945642312, 31134530, 4564078670]
for duration_1 in my_list:
    if 0 <= duration_1 < 60:
        print (duration_1, 'сек')
    elif 60 <= duration_1 < 3600:
        minutes = duration_1 // 60
        seconds = duration_1 % 60
        print(minutes, 'мин', seconds, 'сек')
    elif 3600 <= duration_1 < 86400:
        hours = duration_1 // 3600
        minutes = (duration_1 - hours * 3600) // 60
        seconds = duration_1 % 60
        print(hours, 'час', minutes, 'мин', seconds, 'сек')
    elif 86400 <= duration_1:
        days = duration_1 // 86400
        hours = (duration_1 - days * 86400) // 3600
        minutes = ((duration_1 - days * 86400) - hours * 3600) // 60
        seconds = duration_1 % 60
        print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
    else:
        print('Время не может идти вспять))')
