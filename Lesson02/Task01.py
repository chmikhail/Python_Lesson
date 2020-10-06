# Делаем список
spisok = (4, "jone", 3.15)
#Задаем стартовый инлекс
start_index = 0
# Получаем последний индекс
end_index = len(spisok) - 1
while start_index <= end_index:
    print(f"Индекс",start_index," имеет тип данные: ", type(spisok[start_index]))
    start_index = start_index + 1
