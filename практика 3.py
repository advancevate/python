#Задание 1
x = float(input("Введите минуты\n"))
print(x/60
     
#Задание 2
h = int(input("сколько спит ваша соня?\n"))
a = 9
if h < a:
    print("ну да, мало")
if h == a:
    print("а сам то сколько спишь?")
if h > 9:
    print("спишь?!")
  
#Задание 3
import math
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
p = (a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Площадь треугольника: {area:.2f}")

#Задание 4
import math
def calculate_area():
    print("Выберите тип комнаты:")
    print("1. Треугольная")
    print("2. Прямоугольная")
    print("3. Круглая")

    choice = int(input("Введите номер типа комнаты (1/2/3): "))

    if choice == 1:
        # Треугольная комната
        a = float(input("Введите длину стороны a: "))
        b = float(input("Введите длину стороны b: "))
        c = float(input("Введите длину стороны c: "))

        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Площадь треугольной комнаты: {area:.2f}")

    elif choice == 2:
        # Прямоугольная
        length = float(input("Введите длину комнаты: "))
        width = float(input("Введите ширину комнаты: "))
        area = length * width
        print(f"Площадь прямоугольной комнаты: {area:.2f}")

    elif choice == 3:
        # Круглая
        radius = float(input("Введите радиус комнаты: "))
        area = math.pi * (radius ** 2)
        print(f"Площадь круглой комнаты: {area:.2f}")
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
calculate_area()

#Задание 5
sus1 = "Программист"
sus2 = "Программиста"
sus3 = "Программистов"
n = int(input("скока програмеров ин зе рум"))
if n == 0:
    print(n,sus3)
if n == 1:
    print(n,sus1)
if n > 1 and n < 5:
    print(n,sus2)
if n >= 5:
    print(n,sus3)
  
#Задание 6
ticket_number = input("Введите номер билета: ")
first_half = sum(int(digit) for digit in ticket_number[:3])
second_half = sum(int(digit) for digit in ticket_number[3:])
if first_half == second_half:
    print("Счастливый")
else:
    print("Обычный")
