left, right = 0, 8
for rows in range(0, 5):
    for j in range(0, 9):
        if j == left or j == right:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    left += 1
    right -= 1
    print()