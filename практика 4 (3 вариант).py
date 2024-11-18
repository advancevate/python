#Задание 1
a = int(input('Введите число: '))
if a > 0:
    print (a-1,a, a+1)
else:
    a = 1
    print( a)
  
#Задание 2
file= str(input())
if file[-1] == "c":
    print("Word file")
elif file[-1] == "y":
    print("Python file")
elif file[-1] == "t":
    print("Text file")
  
#Задание 3
a = int(input("Введите первую сторону: "))
b = int(input("Введите вторую сторону: "))
c = int(input("Введите третью сторону: "))
if a == b == c:
    print("Ваш треугольник равносторонний")
elif a == b or b == c or a == c:
    print("Ваш треугольник равнобедренный")
else:
    print("Ваш треугольник разносторонний")
