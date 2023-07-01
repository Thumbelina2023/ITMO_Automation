def task_1(a: int, b: float, c: str, d: list, f: bool) -> None:
    return a, "это", type(a), b, 'это', type(b), c, 'это', type(c),  d, 'это', type(d), f, 'это', type(f)
print(task_1(10, 10.5, 'ten',[1,2,3], True))


def task_2(a: list) -> int:
    return a[0:3]
print(task_2([1,2,3,5,8,21]))
print("Это ряд Фибоначи")


def task_3(a: int) -> int:
    return a**2
print(task_3(3))