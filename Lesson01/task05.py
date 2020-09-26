debet = int(input("Введите поступление денежных средст: "))
credit = int(input("Введите расход денежных средст: "))
employees = int(input("Введите количество сотрудников: "))
profit = debet - credit
print(f"Ваша выручка составила {profit}")
profit_peremployees = profit // employees
profitability = (profit / debet) * 100

if profit < 0:
    print("Вы работаете в убыток")
elif profit > 0:
    print(f"Вы работаете в прибыль. Рентабильность составила {profitability}%.")
print(f"На каждого сотрудника доход составил {profit_peremployees}")

