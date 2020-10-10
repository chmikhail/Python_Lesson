# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Делить на ноль нельзя"



one_input = int(input("Введите первое число: "))
two_input = int(input("Введите второе число: "))

print(division(one_input, two_input))
