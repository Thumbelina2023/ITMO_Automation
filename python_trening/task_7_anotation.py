a: int = 5
b: str = 'строка'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return ' '* (max(0, width- len(s)))+ s
print(indent('123', 123))

#задача 3

def z3(s:str='') -> int:
    return len(s)
print(z3())

def z3_1(a:list, b:list) -> int:
    return max(len(a), len(b))


print(z3_1([1], [2, 4]))

#задача 4
def z4(d):
    d.append(4)
    return d

print(z4([1,2,3]))


#задача 4_1
def z4_1(d:list) -> int:
    return sum(d)
print(z4_1([1,2,3,4]))

#задача 4_2
def z4_1(d:list) -> int:
    rez = 0
    for elem in d:
        rez = rez + elem
    return rez

print(z4_1([1,2,3,4]))