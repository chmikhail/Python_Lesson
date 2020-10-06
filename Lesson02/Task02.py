spisok = list(input("Введите список без пробелов:"))
spisok[1::2],spisok[:-1:2]=spisok[:-1:2],spisok[1::2]
print(spisok)

