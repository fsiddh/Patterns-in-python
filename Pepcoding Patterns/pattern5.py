x = int(input())
left = x // 2
right = x // 2

for i in range(0, x):
    for j in range(0, x):
        if left == j or right == j:
            print('*', end='\t')
        else:
            print('', end='\t')
    print()
    if i < x//2:
        left -= 1
        right += 1
    else:
        left += 1
        right -= 1