def calculate(man_hour, cost_man_hour, priz):
    try:
        return (man_hour * cost_man_hour) + priz
    except TypeError:
        print("Ошибка расчета")