x = int(input())
left = 0
right = x

for i in range(1, x+1):
    for j in range(1, i+1):
        if left < j or right > j: 
            print(j, end='\t')
        else:
            print('', end='\t')
    print()