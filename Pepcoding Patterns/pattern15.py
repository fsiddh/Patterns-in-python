n = int(input())
spaces = n // 2
x = 1
digits = 1

for i in range(0, n):
    for sp in range(0, spaces):
        print('\t', end='')
    cval = digits
    for j in range(0, x):
        print(cval,'\t', end='')
        if j < x//2:
            cval += 1
        else:
            cval -= 1

    if i < n//2:
        spaces -= 1
        x += 2
        digits += 1
    else:
        spaces += 1
        x -= 2
        digits -= 1
    print()