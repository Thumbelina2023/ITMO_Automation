num = 1
if num >= 0:
    print("Число больше либо равно 0")
else:
    print("Число отрицательное")

str_1 = 'test'
str_2 = 'test1'

if str_1 in str_2:
    print('Да')
else:
    print('Нет')

num_float = -3.4
if num_float > 0:
    print('Положительное чсло')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательно')

p_p = True
if num > 0 and p_p:
    print('num - положительное число')
elif not p_p:
    print('Печать запрещена')

a = 5
if 1 >= a <= 4:
    print('Бакалавр')
elif 5 >= a <= 6:
    print('Магистр')
elif 7>= a <= 9:
    print('Аспирант')
else:
    print('Введите корректный код')

#def s_r (year):
#    if year in range(1,5)
#        print('bacalavr')
#    elif year in range

b = 101
#if b > 100 or b < -100:
#    print('-')
#else:
#    print('+')

if b in range(-100, 100):
    print('-')
else:
    print('+')