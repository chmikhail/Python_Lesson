mount_in = int(input("Введите номер месяца: "))
season_list = ["зима", "весна", "лето", "осень"]
season_dict = {0: "зима", 1: "весна", 2: "лето", 3: "осень"}
index = (mount_in % 12) // 3
season_spisok=season_list[index]
season_slovar=season_dict.get(index)
print(f"Списком:",season_spisok)
print(f"Словарем:",season_slovar)

