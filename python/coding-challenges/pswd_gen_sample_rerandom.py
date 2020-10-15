import random
name = input("Please enter your name: ").lower()

mylist = list(name)
pswd1 = random.sample(mylist, k=3)

pswd2 = ""
for i in pswd1:
    pswd2 += i
    
#print(pswd2)

a = random.randrange(0, 10)
b = random.randrange(0, 10)
c = random.randrange(0, 10)
d = random.randrange(0, 10)
num=""
num = str(a) + str(b) + str(c) + str(d)

pswd = pswd2 + num
pswdlist = list(pswd)
pswd3 = random.sample(pswdlist, k=7)

#print(*pswd3, sep = "")
#print ("\n".join(pswd3))
#print ("".join(pswd3))

pswd4 = ""
for i in pswd3:
    pswd4 += i

print(pswd4)
