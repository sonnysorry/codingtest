name = "JAAZ"
count = 0
a_count = 0
c = []

for char in name:
    c.append(min((ord(char) - ord("A")), (91 - ord(char))))
if 'A' not in name:
    answer = len(name) - 1 + sum(c)
if 'A' in name:
    for i in range(0, len(name)):
        name[i]


answer = count - 1
print(answer)