count = 0
#count1 = 0
array = []
sequencelist = ["first", "second", "third", "fourth", "fifth"]
while count < 5:
  #count1 += 1
  #count1 = str(count1)
  x = 'Please enter the ' + sequencelist[count] + ' number: '
  number= int(input(x))
  array.append(number)
  count = count + 1
  #count1 += 1
  #count1 = int(count1)

largest = array[0]
for i in array:
    if i > largest:
        largest = i

print(largest)