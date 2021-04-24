from rectangle import Rectangle


def users_input():
    while True:
        A = input("Введите 4 значения через пробелы в порядке (x, y, width, height):")
        a = A.split()

        if len(a) != 4:
            print("Введите 4 значения")
            continue
        if not (a[0].isdigit() and a[1].isdigit() and a[2].isdigit() and a[3].isdigit()):
            print("Введите числа")
            continue
        x, y, w, h = map(int, a)
        if not (x >= 0 and y >= 0 and w >= 0 and h >= 0):
            print("Введите положительные числа")
            continue
        break
    return x, y, w, h


X, Y, W, H = users_input()

rect_1 = Rectangle(X, Y, W, H)

print(rect_1.get_str())
