a = int(input("Введіть число в діапазоні від 1 до 100 для А: "))
b = int(input("Введіть число в діапазоні від 1 до 100 для В: "))

if a < 1 or a > 100 or b < 1 or b > 100:
    print("Число повинне бути в діапазоні від 1 до 100")
elif a > b:
    print("X =", a/b+1)
elif a < b:
    print("X =", (a-b)/a)
else: print("X =", -2)