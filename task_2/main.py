N = 30

sum = 0
count = 0

print("Число", " ", "Сума")
for i in range(1, N + 1):
    sum += 1 / i
    count += 1
    print(i, " " * 5, sum)

print(f"Сума членів ряду S для N={N}: {sum:.4f}")
print(f"Кількість членів ряду S для N={N}: {count}")