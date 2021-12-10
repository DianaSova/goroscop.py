from datetime import datetime
print('Узнай, сколько времени ты существуешь.')
def Check(Prompt, Min, Max):
    while True:
        D = input(Prompt)
        try:
            D = int(D)
            if D >= Min and D <= Max:
                return D
        except:
            pass
        print('Вы ввели некорректные данные. Попробуйте еще раз.')
def Data(day, month, year):
    JD = day + (153*month + 2) / 5 + 365*year + year / 4 - year / 100 + \
    year / 400 - 32045
    return JD
A = Check('Введите год Вашего рождения:', -9999, 9999)
B = Check('Введите месяц Вашего рождения:', 1, 12)
if A % 4 == 0:
    E = 1
else:
    E = 0
Days=[31, 28+E, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
C = Check('Введите день Вашего рождения:', 1, Days[B-1])
now = datetime.date(datetime.now())
now = Data(now.day, now.month, now.year)
print(f'Прошло {datetime.now().year} лет, или {now} дней, или {now*23.9344444444} '
      f'часов от начала нашей эры.')
F = now - Data(C, B, A)
if F == 0:
    print('Все ясно, автору 0 лет')
if F > 0:
    print(f'Прошло {datetime.now().year - A} лет или {F} дней, или'
          f' {F*23.9344444444} часов, или {F*23.9344444444*60} минут, '
          f'или {F*23.9344444444*60*3600} секунд со дня Вашего рождения.')
if F < 0:
    print(f'До Вашего рождения осталось {-(datetime.now().year - A)} лет, '
          f'или {-F} дней, или {-(F*23.9344444444)} часов, или '
          f'{-(F*23.9344444444*60)} минут, или {-(F*23.9344444444*60*3600)}'
          f' секунд.')
