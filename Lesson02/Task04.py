print("Введите ваш текст,")
spisok = list(map(str, input("для проверки пишите текст с словом больше 10 символов и нескоко пробелов : ").split()))
for i, spisok in enumerate(spisok):
    print(i + 1, spisok[:10])
