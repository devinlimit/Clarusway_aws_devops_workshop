import random
name = input("Please enter your name: ").lower()

namelist = list(name)
namelist1 = []

j = 1
while j < 4:
    x = random.choice(namelist)
    namelist1.append(x)
    #print(namelist1)
    namelist.remove(x)
    #print(namelist)
    j += 1

pswd = ""
for k in namelist1:
    pswd += k
#print(pswd)

a = random.randrange(0, 10)
b = random.randrange(0, 10)
c = random.randrange(0, 10)
d = random.randrange(0, 10)
num=""
num = str(a) + str(b) + str(c) + str(d)

pswd = pswd + num
print(pswd)
