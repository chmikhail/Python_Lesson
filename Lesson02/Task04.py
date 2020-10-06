
spisok = list(map(str, input("Введите ваш текст: ").split()))
for i, spisok in enumerate(spisok):
    print(i + 1, spisok[:10])
