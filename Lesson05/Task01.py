# file_task = open('Task01.ini','w')
#
# while string_input :
#     string_input =input("Введите ваш текст: ")
#     file_task.write('string_input\n')


with open('Task01.ini', 'a') as printable:
    start = "start_task"
    while len(start) > 0:
        start = input("Введите ваш текст: ")
        print(start, file=printable)
    else:
        print("Вы не ввели текст. Конец ввода")
