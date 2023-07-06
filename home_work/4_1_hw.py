class Car:
    def __init__(self, color, type, year, power=None):
        self.color = color
        self.type = type
        self.year = year
        self.power = power
    def start(self):
        if self.power:
            return f'Автомобиль заведен'
        else:
            return f'Автомобиль заглушен'
    def car_year(self):
        return f'Год выпуска: {self.year}'
    def car_type(self):
        return f'Тип: {self.type}'
    def car_color(self):
        return f'Цвет: {self.color}'

car_1  = Car('Красный', 'Седан', '2020', True)
car_2 = Car('Синий', 'Пикап','2021', False)
car_3 = Car('Белый', 'Минивэн','2019', True)

print(car_1.start())
print(car_1.car_color())
print(car_1.car_type())
print(car_1.car_year())
print('\n')
print(car_2.start())
print(car_2.car_color())
print(car_2.car_type())
print(car_2.car_year())
print('\n')
print(car_3.start())
print(car_3.car_color())
print(car_3.car_type())
print(car_3.car_year())