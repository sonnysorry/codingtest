input_data = input()

n = []
s = []

for i in input_data:
    if 'A' <= i and i <= 'Z':
        s.append(i)
    else:
        n.append(i)

print(s.sort())
