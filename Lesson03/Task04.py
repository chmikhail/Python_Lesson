def my_func(x, y):
    if y < 0:
        y = -y
        result = 1 / (x ** y)
    else:
        result = (x ** y)
    return print(result)


def my_func_task(x, y):
    if y < 0:
        y = -y
        result = 1
        for _ in range(y): result *= x
        result = 1 / result
    else:
        result = 1
        for _ in range(y): result *= x
    print(result)


x = int(input("Число: "))
y = int(input("Степень: "))/////

print(my_func(x, y))
print(my_func_task(x, y))
