# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
time = int(input('Введите время в секундах: '))
hours = time // 3600
mins = time % 3600 // 60
secs = time % 3600 % 60
print(f'Введенное время: {hours}:{mins}:{secs}')