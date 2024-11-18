#Задание 1
names = ["Richard", "Igor", "Jonathan", "Alice", "Mary", "Bonnie"]
for x in names:
    print(f"hello {x}!")

#Задание 2
phrase = "I'm learning cycles."
for Y in range(10):
    print(phrase)

#Задание 3
stations = ["Малиновка", "Рябиновка", "Суслово", "Дрожжино", "Звягино"]
for t in stations:
    print(f"train on station: {t}")

#Задание 4
shop = ["Laptop", "Smartphone", "Watch", "Tablet", "Headphones"]
for i in shop:
    print(i)
    if i == "Laptop":
        print("I'm buying this.")
    else:
        print("I don't need it.")

#Задание 5
tasks = ["Сдать проект (Важная)", "Сходить в магазин", "Позвонить врачу (Важная)", "Убраться в комнате",
         "Подготовить отчёт"]

for i, x in enumerate(tasks, start=1):
    if "Важная" in x:
        print(f"{i}!: {x} ")
    else:
        print(f"{i} : {x}")

#Задание 6
tsb = 0
abc = int(input('Введите количество чисел:'))
for num in range(abc):
    print('Введите сами числа:')
    vvs = int(input())
    tsb = tsb + vvs
print('Сумма чисел = ', tsb)

#Задание 7
steps = 10

for x in range(steps):
    print(f"цикл сработал {x} раз")

#Задание 8
while True:
    bdsm = str(input(">"))
    if bdsm == "w":
        print("фраер идёт вперёд")
    elif bdsm == "a":
        print("фраер едёт налево")
    elif bdsm == "s":
        print("фраер едёт назад")
    elif bdsm == "d":
        print("фраер едёт вправо")
    elif bdsm == "stop":
        print("завершить программу")
        break
    else:
        print("Отставить")
#Задание 9
while True:
    a = int(input("Введите число от 1 до 9: "))
    if a < 1 or a > 9:
        print("число вне диапазона")
    else:
        break
b = 1
while b <= 10:
    c = a * b
    print(f"{a} * {b} = {c}")
    b += 1

#Задание 10
print('Загадка: Сау Сау Музыкант, певец, рассказчик - А всего труба да ящик.\nОтвет:')
ya3 = 3
while ya3 > 0:
    za = str(input(''))
    if za == 'граммофон':
            print('Загадка разгадана. Поздравляю!')
            break
    else:
        ya3 = ya3 - 1
    print('Сау Неправильно!')
    print('Сау Попыток осталось: Сау', ya3)
