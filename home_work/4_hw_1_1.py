class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return f'Автомобиль заведен'
    def stop(self):
        return f'Автомобиль заглушен'
    def car_year(self):
        return f'Год выпуска: {self.year}'
    def car_type(self):
        return f'Тип: {self.type}'
    def car_color(self):
        return f'Цвет: {self.color}'

car_1 = Car('Красный', 'Седан', '2020')
car_2 = Car('Синий', 'Пикап','2021')
car_3 = Car('Белый', 'Минивэн','2019')

print(car_1.start())
print(car_1.stop())
print(car_1.car_type())
print(car_1.car_color())
print(car_1.car_year())
print('\n')
print(car_2.start())
print(car_2.stop())
print(car_2.car_type())
print(car_2.car_color())
print(car_2.car_year())
