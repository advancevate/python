#Задание 1
age = int(input("Введите ваш возраст: "))
if age<18:
    print("Вы несовершеннолетний")
elif 18<= age <=65:
    print("Вы трудоспособный человек")
else:    print("Вы пенсионер")

#Задание 2
x = int(input("Введите стоимость покупки: "))
if x<1000:
    print("Скидка не предоставляется")
elif 1000<= x <=5000:
    print("Скидка 5%")
else:
    print("Скидка 10%")

#Задание 3
z = int(input("введите первое число: "))
x = int(input("введите второе число: "))
c = int(input("выберите операцию:\n1: +\n2: -\n3: *\n4: /\n"))
if c == 1:
    print("ответ: ", z + x)
elif c == 2:
    print("ответ: ", z - x)
elif c == 3:
    print("ответ: ", z * x)
elif c == 4:
    print("ответ: ", z / x)
else:
    print("Неверная операция")

#Задание 4
x = int(input("Введите число: "))
if x % 2 == 0 and "x"[-1] == 2 or "x"[-1] == 6:
    print("True")
else:
    print("False")

#Задание 5
password = 192837465
n = int(input("Введите пароль: "))
if n == password:
    print("Доступ разрешен ")
else:
    print("Неверный пароль ")

#Задание 6
x = input("Введите координаты квадрата: ")
if x == "B1" or x == "B3" or x == "B7" or x == "C1" or x == "C4" or x == "C5" or x == "C6" or x == "C8" or x == "C9":
    print("В данном квадрате обитает синий попугай")
elif x == "B2" or x == "B4" or x == "B6" or x == "B8" or x == "C2" or x == "C7" or x == "C10" or x == "C11":
    print("В данном квадрате обитает зеленый попугай")
else:
    print("квадарат пустой")

#Задание 7
n = int(input("Введите число: "))
k = int(input("Введите второе число: "))
if n % k == 0:
    print("кратно")
else:
    print("не кратно")

#Задание 8
lvl = int(input("введите ваш уровень: "))
hp = int(input("введите ваше здоровье: "))
if lvl<0 or hp>100:
    print("некорректные данные")
else:
    if lvl<5:
        print("ваш уровень слишком низкий для выполнения миссии")
    else:
        if hp > 50:
            print("вы готовы к миссии!")
        elif 20 < hp:
            print("ваше здоровье низкое, будьте осторожны")
        else:
            print("ваше здоровье слишком низкое для выполнения миссии")

#Задание 9
inventory = ["яблоко", "шариковая ручка"]
if "ключ" in inventory and "фонарь" in inventory:
    print("вы можете пройти через дверь")
elif "ключ" not in inventory and "фонарь" in inventory:
    print("у вас нет ключа, вы не можете открыть дверь")
elif "ключ" in inventory and "фонарь" not in inventory:
    print("у вас нет фонаря, слишком темно, чтобы пройти")
else:
    print("у вас нет ни ключа, ни фонаря, вы не можете пройти через дверь")

#Задание 10
king = "Enemies are coming! Are the archers ready?"
warrior = "For the Alliance!"
magician = "The spell is ready."
if king [-1] == "?" or king [-1] == "!" or king [-1] == ".":
    print("знак имеется")
else:
    print("знака нет")
if warrior [-1] == "?" or warrior [-1] == "!" or warrior [-1] == ".":
    print("знак имеется")
else:
    print("знака нет")
if  magician [-1] == "?" or magician [-1] == "!" or magician [-1] == ".":
    print("знак имеется")
else:
    print("знака нет")
