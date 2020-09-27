number = int(input("Введите число: "))
lost = number % 10
while number > 0:
    value = number % 10
    if value > lost:
        lost = value
    number = number // 10
print(lost)