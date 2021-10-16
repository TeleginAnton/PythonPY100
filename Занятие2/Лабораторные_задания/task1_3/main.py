# TODO
a = int(input('Число A: '))
b = int(input('число b: '))

if a ** 2 + b ** 2 > (a + b) ** 2:
    print('суммв квадратов больше')
elif a ** 2 + b * 2 < (a + b) ** 2:
    print("Квадрат суммы больше")
else:
    print('Суммы равны')