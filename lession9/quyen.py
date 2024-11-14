QqAa = open("sesame.txt", "w")
points = 0

abc = int(input("What number is this question? 1: 1, 2: 2, 3: 3, 4: 4;   "))
aAqQ = QqAa.write(str(abc)+" ")

defg = int(input("What number is this question? 1: 1, 2: 2, 3: 3, 4: 4;   "))
aAqQ = QqAa.write(str(defg)+" ")

hij = int(input("What number is this question? 1: 1, 2: 2, 3: 3, 4: 4;   "))
aAqQ = QqAa.write(str(hij)+" ")

klmn = int(input("What number is this question? 1: 1, 2: 2, 3: 3, 4: 4;   "))
aAqQ = QqAa.write(str(klmn))
QqAa.close()

QqAa = open("sesame.txt", "r")
RrNn = QqAa.readlines()
# print(RrNn)
a = RrNn[0].split(" ")
for n in range(1, 5):
    # print(n)
    if int(a[n-1]) == n:
        points += 1

if points == 4:
    print("You win")
else:
    print("You lost hah hah")
