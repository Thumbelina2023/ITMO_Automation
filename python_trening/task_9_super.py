class A:
    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x +5

b=B()
print(B().y)
print(b.y)


class BasePage:
    def __init__(self, base_url):
        self.base_url = base_url

    def visit(self):
        return f'Выполен вход по урлу + {self.base_url}'

class HomePage(BasePage):
    def __init__(self, base_url):
        super().__init__(base_url)

home = HomePage('http://moda.com')

print(home.visit())