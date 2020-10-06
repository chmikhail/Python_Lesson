print("Введите ваш текст,")
spisok = list(map(str, input("для проверки пишите текст больше 10 мисволов слово и нескоко пробелов : ").split()))
for i, spisok in enumerate(spisok):
    print(i + 1, spisok[:10])
