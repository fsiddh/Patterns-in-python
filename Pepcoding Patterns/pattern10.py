x = int(input())

left = x//2
right = x//2
if x % 2 != 0:
    t=x;
else:
    t=x+1;
for i in range(0, t):
    for j in range(0, t):
        if j == left or j == right:
            print('*', end='\t')
        else:
            print('', end='\t')
    print()
    if i >= t//2:
        left += 1
        right -= 1
    else:
        left -= 1
        right += 1