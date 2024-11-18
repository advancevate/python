#Задание 1
mtx = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print("матрица:")
for i in mtx:
    print(i)
x = []
y = 0
for z in mtx:
    for b in z:
        if b % 2 != 0:
            x.append(b)
        else:
            y += 1
print("Все нечётные числа матрицы:\n", x)
print("Кол-во чётных чисел", b)

#Задание 2
mtx1 = [[2,4,3,6],[5,7,1,5]]
mtx2 = [[2,9,0,2],[3,4,7,6]]
answer = [[0,0,0,0],[0,0,0,0]]
for row in range(len(answer)):
    for elem in range(len(answer[0])):
        answer[row][elem] = mtx1[row][elem] * mtx2[row][elem]
sum1 = 0
sum2 = 0
for i in answer[0]:
    sum1 += i

for i in answer[1]:
    sum2 += i
print(f"{answer}\n{answer[0]} summa stroki: {sum1}\n{answer[1]} summa stroki: {sum2}")

#Задание 3
frt = [["Banana","apple"],["apricot", "Avocado"],["lime","lemon"],["Mango","grapes"]]
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = []
for row in frt:
    for element in row:
        if element[0] in up:
            answer.append(element)
print(answer)

#Задание 4
random_elements = [['toy', 'bee', 'cheese', 'ear'],
[False, 'word', '0110110', 10],
['happiness', '(」°ロ°)」', 'luck', None],
['car', '<- code ->', 4.7, True]]
for i in random_elements:
    for index, element in enumerate(i):
        if index % 2 == 0:
            print(f"Индекс: {index}, Элемент: {element}")
