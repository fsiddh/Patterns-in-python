#Method 1
spaces = 0
for i in range(0, 5):
    for j in range(0, 5):
        if j == spaces:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    spaces += 1

# Method 2
for i in range(0, 5):
    for j in range(0, 5):
        if j == i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()