import random
s_b = [0 , 0]
count = 0
while True:
    rand = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    a = random.choice(rand)
    rand.remove(a)
    b = random.choice(rand)
    rand.remove(b)
    c = random.choice(rand)
    rand.remove(c)
    #print(a, b, c)
    x = str(input("Guess : "))
    guess = []
    for i in x:
        guess.append(i)
    #print(guess)
    if guess[0] == a and guess[1] == b and guess[2] == c:
        s_b[0] += 1
    else:
        s_b[1] += 1
    count += 1
    print(str(s_b[0])+ "S" + str(s_b[1]) + "B")

    if (s_b[0] == 3 or s_b[1] == 4):
        print("score : %d" %count)
        break;