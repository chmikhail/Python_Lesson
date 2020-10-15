# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
# произведения всех элементов списка.
from functools import reduce

items = [x for x in range(99, 1001) if x % 2 == 0]
print(items)
sum_all = reduce(lambda x, y: x + y, items)
print(sum_all)
