
def month_to_season(month):
    if month in [12, 1, 2]:
        return "Эима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Некорректный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))
