# Делаем список
spisok = (4, "jone", 3.15)
start_index = 0
end_index = len(spisok) - 1
while start_index <= end_index:
    print(f"Индекс",start_index," имеет тип данные: ", type(spisok[start_index]))
    start_index = start_index + 1
