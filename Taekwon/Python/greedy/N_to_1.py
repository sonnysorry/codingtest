a, b = map(int, input().split())
count = 0

while True:
    if(a == 1):
      print(count)
      break
    elif(a % b != 0):
        a = a - 1
        count = count + 1
    elif(a % b == 0):
        a /= b
        count = count + 1
