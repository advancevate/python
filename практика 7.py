#Задание 1
data = [["folder", "coursework.doc", "folder", "pict.png", "data.accdb"],
        ["icon.ico", "script.js", "index.html", "style.css", "prog.py"],
        ["my_song.mp3", "anapa-2003.png", "cs_1.6.exe", "folder", "cheat.txt"],
        ["notes.txt", "main.py", "work.pdf", "cartoon.mp4", "array.py"],
        ["project.psd", "cycle.py", "folder", "cycle.js", "turtle.py"]]
python = ""
javascript = ""
print("начальный список")
for i in data:
    print(i)
for row in data:
    i = 0
    while i != len(row):
        elem = row[i]
        if elem == "folder":
            row.pop(i)
            i -= 1
        if elem == "data.accdb":
            row[i] = "data.sql"
        if ".py" in elem:
            python += elem + " "
        if ".js" in elem:
            javascript += "new_" + elem + " "
        i += 1
print("\nбез папок и с заменой data")
for i in data:
    print(i)
print(f"\nвсе файлы.py:\n{python}")
print(f"\nвсе new_файлы.js:\n{javascript}")

#Задание 2 
word_numb = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
user = int(input("введите число от 0 до 9: "))
if user < 0 or user > 9:
    print("Неверное число")
for i in range(user + 1):
    print(word_numb[i])
    
#Задание 3
bin_sy = ["11011111", "11011101", "11000111", "11011100", "11011110"]
xx = []
for i in bin_sy:
    print(int(i, 2))
    xx.append(int(i, 2))
print(f"макс. значение - {max(xx)}")
print(f"мин. значение - {max(xx)}")
