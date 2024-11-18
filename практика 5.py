#Задание 1
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', 10]
for item in m[:]:
    if not isinstance(item, str):
        m.remove(item)
print(m)

#Задание 2
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1:5]
print(abc)

#Задание 3
numbers = [1, 4]
numbers.insert(1, 2)
numbers.insert(2, 3)
print(numbers)

#Задание 4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass = [num for num in mass if num >= 0]
sort = sorted(mass)
sort_rev = sorted(mass, reverse=True)
print(sort)
print(sort_rev)

#Задание 5
# Инициализация списков
negative_numbers = []
positive_numbers = []
pirog = []
count = int(input("Введите количество чисел: \n"))
for _ in range(count):
    number = float(input("Введите число: \n"))
    if number < 0:
        negative_numbers.append(number)
    elif number > 0:
        positive_numbers.append(number)
    else:
        pirog.append(number)
negative_sum = sum(negative_numbers)
positive_average = sum(positive_numbers) / len(positive_numbers) if positive_numbers else 0
pirog = ['*' if x == 0 else x for x in zeros]
print(negative_sum)
print(positive_average)
print(f"Количество звёзд: {len(zeros)}, {zeros}")
