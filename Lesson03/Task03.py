def my_func(a, b, c):
    max = a
    if max > b:
        max = b
    if max < c:
        max = c
    return max


a_i = int(input("Введите первое число:"))
b_i = int(input("Введите второе число:"))
c_i = int(input("Введите третье число:"))

print(f"Максимальное чило из введеных: {my_func(c=c_i, b=b_i, a=a_i)}")
# Просто вывод числа
# print((my_func(a=a_i, b=b_i, c=c_i)))
