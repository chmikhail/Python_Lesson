number = int(input("Введите число: "))
a = number
b = []
while a > 0:
  b.append(a % 10)
  a = a // 10
b = b[::-1] # так можно развернуть, если бы нам был важен порядок
result=max(b)
print(result)