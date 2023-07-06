from task_9_checks import Checks
class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text
search = Input('input#search', 'Найти')
catalog = Input('Каталог', 'Текст')

print(search.loc)
print(catalog.text)
print(search.check_text())
print('\n')

class Button(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.loc = loc
        self.text = text
exit = Button('Выход', 'button#exit')
find = Button('Ввод', 'button#find')
print(exit.loc)
print(find.text)
print(exit.check_text())
print('\n')

class Title(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.loc = loc
        self.text = text
zagolovok = Title('', 'title#zagolovok')
a= Title('Welcome', 'title#a')

print(zagolovok.loc)
print(a.text)
print(a.check_text())