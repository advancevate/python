#Задание 1
my_dict = {1:'0101101', 2:'101110', 3:'1A14C', 4:'1100100', 5:'101010'}
print(my_dict)
my_dict.pop(3)
print(my_dict)
my_dict['10'] = '0100101'
print(my_dict)

#Задание 2
sl = {"</>": 13, "script": 1, "___init___": 10, "seld": 5, "number_9": 6, "#comment": 100}
print(sl)
key = input("введите ключ: ")
val = input("введите значение: ")
sl[key] = val
print(sl)

#Задание 3
ty = {}
while len(sl) != 3:
    k = input("введите новый ключ: ")
    v = input("введите новое значение: ")
    ty[k] = v
print(ty)

#Задание 4
all_d = {1:15, 4:80, 44:0, 256:15, 100:70, 101:70, 20:44, 3:9}
del_key = [1, 101, 3]
for i in del_key:
    all_d.pop(i)
print(all_d)
