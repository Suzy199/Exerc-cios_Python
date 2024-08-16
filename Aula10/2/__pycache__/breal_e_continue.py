for num in range(10):
    if num <= 5:
        print(num, end=' ')
    else:
        break
    
num = 0    
while True:
    print(num, end='')
    if num == 10:
        break
    elif num % 2 != 0:
        continue
    num += 1