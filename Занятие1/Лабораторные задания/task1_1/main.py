DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input('Год родения: ')) # TODO запросить у пользователя год рождения
current_year = int(input('Текущий год:'))  # TODO запросить у пользователя текущий год

dyas = (start_year - current_year) * DAYS_OF_YEAR
print(dyas)
