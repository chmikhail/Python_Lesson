day_km = int(input("Введите ваш результат в первый день: "))
finish_km = int(input("Какой результат в километрах хотите достич: "))


while day_km < finish_km:
    print("Ваш результат за день: ", day_km )
    day_km = day_km * 1,1
else:
    print("Вы достигли резултата ")
