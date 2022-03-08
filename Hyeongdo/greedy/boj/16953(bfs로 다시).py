# A -> B

a, b = map(int, input().split())

count = 0
task = 0
while(True):
    if b == a:
        break
    
    if b % 2 == 1:
        temp = str(b)[:-1]
        if temp == '':
            task = 1
            break
        b = int(temp)
    else:
        temp_1 = int(b)//2
        b = temp_1 
    count += 1

if count == 1 or task == 1:
    print(-1)
else:
    print(count + 1)