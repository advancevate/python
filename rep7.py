#Задание 1
def create_car(brand: str, color: str, max_speed: int) -> str:
    return(f"марка: {brand}, цвет: {color}, макс скрость: {max_speed} км/ч")
car_1 = create_car("McLaren", "black", 500)
car_2 = create_car("Tesla", "white", 270)
print(car_1)
print(car_2)

#Задание 2
def switch_check(switch: bool):
    if switch == True:
        print("True работает")
    elif switch == False:
        print("False не работает")
    else:
        print(f"{switch} сломан")

switch1 = True
switch2 = False
switch3 = None

switch_check(switch1)
switch_check(switch2)
switch_check(switch3)

#Задание 3
