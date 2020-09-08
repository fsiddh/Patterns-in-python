# Method 1
for rows in range(0, 5):
    for j in range(0, 9):
        if j == 4-rows or j == rows+4:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Method 2

left, right = 4, 4
for rows in range(0, 5):
    for j in range(0, 9):
        if j == left or j == right:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    left -= 1
    right += 1
    print()