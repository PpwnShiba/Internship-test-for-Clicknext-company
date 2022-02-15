

numOfDay = int(input("Enter total of Days : "))

dateArray = []
for i in range(0, numOfDay):
    inputDate = int(input("Enter date["+str(i)+"] : "))
    dateArray.append(inputDate)
print('Array of date = ', dateArray)
positiondate = 0
check = 1

for i in range(0, numOfDay-1):
    if(dateArray[i+1] - dateArray[i] == 1):
        check = check+1
print(check)

# else:
for i in range(0, numOfDay-1):
    positiondate = positiondate+1
    if(dateArray[i+1] - dateArray[i] == 1):
        print(dateArray[positiondate-1], end="-")
    elif(dateArray[i+1] - dateArray[i] > 1):
        print(dateArray[positiondate-1], end=",")
print(dateArray[numOfDay-1])
