count = 0
#count1 = 0
array = []
sequencelist = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"]
a = int(input("How many stock prices does your array include? (Please enter in digit): "))
while count < a:
  #count1 += 1
  #count1 = str(count1)
  x = 'Please enter the ' + sequencelist[count] + ' number: '
  number= int(input(x))
  array.append(number)
  count = count + 1
  #count1 += 1
  #count1 = int(count1)

smallest = array[0]
for i in array:
    if i < smallest:
        smallest = i

#print(smallest)

largest = array[0]
for i in array:
    if i > largest:
        largest = i

#print(largest)

profit = largest - smallest
print(profit)