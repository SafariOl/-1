n = 5
for row in reversed(range(n)):
    for col in reversed(range(5 - row, 6)):
        print(col, end=" ")
    print("\n")
    
