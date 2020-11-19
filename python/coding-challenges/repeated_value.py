products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]
#print(products)
newlist = []
newlist = products.copy()
#print(newlist)
newlist1 = []
newlist2 = []
x = 0
y = 0
z = len(newlist)
#print(z)
while z > 0:
    
    for i in newlist:
        products.pop(0)
        products = products + newlist1
        
        #products.pop(0)
        #print(len(newlist))
        #print(len(products))
        if i in products:
            newlist1.append(i)            
        else:
            newlist2.append(i)
            #print(i)
        x = x + 1
    z = z - 1
finalset = set(newlist2)
finallist = list(finalset)
#print(finallist)
#print(finalset)
#for i in finalset:
#   print(i)
#print(newlist2)
for i in newlist:
    if i in finallist:
        print(i)
    