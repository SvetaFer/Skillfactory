def greet ():
    print ("Добро пожаловать в игру крестики нолики!")
    print("Немного правил:")
    print("1) значения вводятся в формате координат")
    print("х - номер строки")
    print("у - номер столбца")
    print(" ----------------------------------------")
    print("Хорошей игры!")

greet ()

field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
def show ():
    print (f"   0 1 2")
    for i in range (3):
        print (f" {i} {field [i] [0]} {field [i] [1]} {field [i] [2]}")

def ask ():
    while True:
        x, y = map (int, input ("Твой ход. Введи две координаты:"). split ())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field [x] [y] == " " :
                return x, y
            else:
                print ("Ячейка занята")
        else:
            print ("Выход за пределы координат")

def check_win ():
    for i in range (3):
        symbols = []
        for j in range (3):
            symbols.append (field [i][j])
        if symbols == ["X", "X", "X"]:
            print ("Выиграл Х!!!")
            return True
        if symbols == ["O", "O", "O"]:
            print ("Выиграл O!!!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х!!!")
            return True
        if symbols == ["O", "O", "O"]:
            print ("Выиграл O!!!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ["X", "X", "X"]:
        print("Выиграл Х!!!")
        return True
    if symbols == ["O", "O", "O"]:
        print("Выиграл O!!!")
        return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
    if symbols == ["X", "X", "X"]:
        print("Выиграл Х!!!")
        return True
    if symbols == ["O", "O", "O"]:
        print("Выиграл O!!!")
        return True
    return False

num = 0
while True:
    num += 1
    show()
    if num %2 == 1:
        print ("Ходит Крестик")
    else:
        print ("Ходит нолик")

    x, y = ask ()
    if num %2 == 1:
        field [x] [y] = "X"
    else:
        field[x][y] = "O"

    if check_win ():
        break

    if num == 9:
        print("Ничья")
        break

