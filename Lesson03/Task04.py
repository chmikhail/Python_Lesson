def my_func(x, y):
    y = -y
    result = 1 / (x ** y)
    return print(result)

def my_func_task(x, y):
    y = -y
    result = 1
    for _ in range(y): result *= x
    result = 1 / result
    print(result)


x = int(input("Число: "))
y = int(input("Степень: "))

print(my_func(x, y))
print(my_func_task(x, y))

