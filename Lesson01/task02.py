input_seconds = int(input("Введите время в секундах: "))
seconds = input_seconds % 60
minutes = input_seconds // 60
hour = input_seconds // 3600
print(f"{hour}:{minutes}:{seconds}")