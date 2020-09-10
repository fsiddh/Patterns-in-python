x = int(input())

digits = 1 
for i in range(0, x):
    for j in range(0, i+1):
        print(digits, end='\t')
        digits += 1
    print()
