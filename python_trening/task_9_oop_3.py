class Soda:
    def __init__(self, ing = None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и + {self.ing}')
        else:
            print('Обычная газировка')


bezdobavka = Soda()
dobavki = Soda('Малина')

bezdobavka.show_my_drink()
dobavki.show_my_drink()