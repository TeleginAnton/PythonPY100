# Напишите ваше решение

speed = int(input('Скорость передачи данных: '))
coast = int(input('Стоимомть: '))
time = int(input('Врмя скачивания '))
a = speed * 1024
b = (time / a) * 1024 * 1024 * 1024
c = (b - (1024 * 3)) * coast
print(b, c)