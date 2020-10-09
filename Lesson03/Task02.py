# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_data_write(fname, sname, bday, city, mail, fnumber):
    print(f"Ваши данные:{fname} {sname} {bday}. А так же {mail} {city} и {fnumber} записаны в базу данных")


fname_i = input("Введите ваще имя:")
sname_i = input("Введите ваще фамилию:")
bday_i = input("Введите ваще День рождения:")
mail_i = input("Введите ваще e-mail:")
cyti_i = input("Введите ваще город:")
fnumber_i = input("Введите ваще Сотовый телефон:")

user_data_write(fnumber=fnumber_i, fname=fname_i, sname=sname_i, bday=bday_i, mail=mail_i, city=cyti_i)
