text1 = input("Please enter a stirng: ")
text = text1 + " "

textlist = list(text)
vowelslist = ["a", "e", "o", "ö", "ı", "i", "u", "ü"]

result = "negative"
j = 0
for i in textlist:
    if i in vowelslist:
        if textlist [j+1] in vowelslist:
            result = "positive"
    j += 1
print(result)
