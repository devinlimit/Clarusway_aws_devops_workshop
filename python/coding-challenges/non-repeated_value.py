products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]
newlist = products.copy()
newlist1 = []
newlist2 = []

for i in newlist:
    products.pop(0)
    products = products + newlist1
    if i in products:
        newlist1.append(i)            
    else:
        newlist2.append(i)
    
for i in newlist2:
    print(i)
