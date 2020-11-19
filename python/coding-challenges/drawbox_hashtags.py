a = int(input("Please enter the digit parameter for the side length of the square box: "))
b = a * "#"
c = a - 2
if a > 1:
    print(b)
    for i in range(c):
        print("#" + c * " " + "#")
    print(b)
if a == 1:
    print("#")
else:
    print("Invalid digit!")