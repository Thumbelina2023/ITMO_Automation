# Задача 1
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def square(self):
        return self.width * self.height

    def perimetr(self):
        return (2*self.width) + (2*self.height)

s_1 = Rect(10, 20)
s_2 = Rect(15, 25)
s_3 = Rect(1024, 256)
print(f'Площадь прямоугольника S1 =  {s_1.square()} м2')
print(f'Периментр прямоугольника S1 = {s_1.perimetr()} м')
print('\n')
print(f'Площадь прямоугольника S2 =  {s_2.square()} м2')
print(f'Периментр прямоугольника S2 = {s_2.perimetr()} м')
print('\n')
print(f'Площадь прямоугольника S3 =  {s_3.square()} м2')
print(f'Периментр прямоугольника S3 = {s_3.perimetr()} м')
print('_'* 125)

# Задача 2

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a/self.b
    def subtraction(self):
        return self.a - self.b

sum = Math(20, 15)
mul = Math(22, 1)
div = Math(100, 50)
sub = Math(5, 3)
print(f'Сумма параметров а и b = {sum.addition()}')
print(f'Произведение параметров а и b = {mul.multiplication()}')
print(f'Частное параметров а и b = {div.division()}')
print(f'Разность параметров а и b = {sub.subtraction()}')
print('_'* 125)

# Задача 3

class Button:
    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return f'Клик по кнопке {self.text}'

button_1 = Button('Text box', 'Кнопка', 'button#box')
button_2 = Button('Check box', 'Кнопка', 'button#cbox')
button_3 = Button('Radio button', 'Кнопка', 'button#r')
button_4 = Button('Web Tables', 'Кнопка', 'button#web')
button_5 = Button('Buttons', 'Кнопка', 'button#b')
button_6 = Button('Links', 'Кнопка', 'button#link')
button_7 = Button('Broken Links - Images', 'Кнопка', 'button#blink')
button_8 = Button('Upload and Download', 'Кнопка', 'button#ud')
button_9 = Button('Dynamic Properties', 'Кнопка', 'button#box')

print(button_1.click())
print(button_2.click())
print(button_3.click())
print(button_4.click())
print(button_5.click())
print(button_6.click())
print(button_7.click())
print(button_8.click())
print(button_9.click())



