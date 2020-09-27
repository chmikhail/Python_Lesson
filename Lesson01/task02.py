input_seconds = int(input("Введите время в секундах: "))
hour = input_seconds // 3600
minutes = (input_seconds//60)%60
seconds = input_seconds % 60
if minutes < 10:
    minutes = str('0' + str(minutes))
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = str('0' + str(seconds))
else:
    seconds = str(seconds)
print(str(hour) + ':' + str(minutes) + ':' + str(seconds))
