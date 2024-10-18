from random import randint

length = 6
final = ""

for j in range (0, length):
    key =""
    for i in range (0, 5): key+=str(randint(1, 6))

    passreader = open('words2.txt', 'r')
    for line in passreader:
        temp = line.strip()
        if temp[0:5] == key: final+=temp[6:]
    passreader.close()
final = "1" + final[0].capitalize() + final[1:] + "!"
print(final)
print(len(final))
