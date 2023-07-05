class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
search = Input('input#search', 'Найти')
catalog = Input('Каталог', 'Текст')

print(search.loc)
print(catalog.text)

class Button:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text
exit = Button('Выход', 'button#exit')
find = Button('Ввод', 'button#find')

class Title:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text
zagolovok = Title('', 'title#zagolovok')
a= Title('Welcome', 'title#a')

