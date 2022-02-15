
numinput = int(input("Enter high of triangle : "))

while(numinput > 4):
    print('Please input only 1 to 4.')
    numinput = int(input("Enter high of triangle : "))

space = ' '
numline = 0
for i in range(numinput, 0, -1):
    numline = numline+1
    print(i*space, end="")
    if(numline == 1):
        for z in range(1, 2):
            print(str(z) + space, end=" ")
    elif (numline == 2):
        for z in range(2, 4):
            print(str(z) + space, end=" ")
    elif (numline == 3):
        for z in range(4, 7):
            print(str(z) + space, end=" ")
    elif (numline == 4):
        for z in range(7, 10):
            print(str(z) + space, end=" ")
        print('0', end="")
    print("\n")
