# 불끄기

light = []
a = [1, -1, 0, 0, 0]
b = [0, 0, 0, -1, 1]
for _ in range(10):
    light.append(input())

arr = [[0]*10]*10
for i in range(10):
    for j in range(10):
        for k in range(len(a)):
            if i+a[k] < 0 or i + a[k] > 10 or j + b[k] < 0 or b[k] > 10:
                light[i+a[k]][j+b[k]]
    
print(arr)
