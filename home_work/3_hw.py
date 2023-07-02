# Задача 1

def chisla(a, b):
    return max(a, b)


print(chisla(2, 20))


# Задача 2


def chisla_2(a, b):
    if a + 135 == b or a - 135 == b:
        print('Yes')

    else:
        print('No')


chisla_2(20, 145)


# Задача 3

def time_year(a: int):
    if a==1 or a==2 or a==12:
        print('Зима')

    elif a in range(3, 6):
        print('Весна')

    elif a in range(6, 9):
        print('Лето')

    elif a in range(9, 12):
        print('Осень')

    else:
        print('Введите правильый месяц года!')

time_year(1)

# Задача 4

def chisla_3(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')
chisla_3(20, 11, 50)

# Задача 5

def spisok(a: list):
    cot = 0
    for i in a:
        if i > 0:
            cot = cot + 1
    print(cot)
spisok([-1, -1, 5, -5, 10])

# Задача 6

def days(a: int, b: int) -> int:
    c = 29
    return a*(12*c) + (b*c)
print(days(2,3))

