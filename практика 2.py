#Задание №1
bat = int(input("Введите кол-во байтов:"))
print(bat * 8)
#Задание №2
S=int(input("Введите кол-во страниц: "))
C=int(input("Введите кол-во строк на странице: "))
N=int(input("Введите кол-во символов на странице: "))
L=S*C*N
print("Книга весит:",L/1024,"Кбайт")
